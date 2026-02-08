"""
OnlyFans AI Manager - Utilities
Helper functions and utilities
"""
from typing import Dict, List, Optional
from datetime import datetime
import json


class FanProfile:
    """Data class for storing fan profile information"""
    
    def __init__(
        self,
        fan_id: str,
        name: Optional[str] = None,
        is_subscriber: bool = False,
        subscription_tier: Optional[str] = None,
        total_tips: float = 0.0,
        content_purchased: int = 0,
        last_interaction: Optional[datetime] = None,
        interests: Optional[List[str]] = None,
        notes: Optional[str] = None
    ):
        self.fan_id = fan_id
        self.name = name
        self.is_subscriber = is_subscriber
        self.subscription_tier = subscription_tier
        self.total_tips = total_tips
        self.content_purchased = content_purchased
        self.last_interaction = last_interaction or datetime.now()
        self.interests = interests or []
        self.notes = notes
    
    def to_context(self) -> Dict:
        """Convert profile to context dictionary for AI"""
        return {
            "is_subscriber": self.is_subscriber,
            "has_tipped": self.total_tips > 0,
            "purchased_content": self.content_purchased > 0,
            "is_vip": self.total_tips >= 100 or self.content_purchased >= 5
        }
    
    def to_dict(self) -> Dict:
        """Convert profile to dictionary"""
        return {
            "fan_id": self.fan_id,
            "name": self.name,
            "is_subscriber": self.is_subscriber,
            "subscription_tier": self.subscription_tier,
            "total_tips": self.total_tips,
            "content_purchased": self.content_purchased,
            "last_interaction": self.last_interaction.isoformat() if self.last_interaction else None,
            "interests": self.interests,
            "notes": self.notes
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'FanProfile':
        """Create profile from dictionary"""
        if data.get("last_interaction"):
            data["last_interaction"] = datetime.fromisoformat(data["last_interaction"])
        return cls(**data)


class MessageLogger:
    """Simple message logger for tracking interactions"""
    
    def __init__(self, log_file: str = "messages.log"):
        self.log_file = log_file
    
    def log_message(
        self,
        fan_id: str,
        message: str,
        response: str,
        message_type: str = "chat"
    ):
        """Log a message interaction"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "fan_id": fan_id,
            "message": message,
            "response": response,
            "type": message_type
        }
        
        try:
            with open(self.log_file, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Warning: Could not write to log file: {e}")
    
    def get_recent_logs(self, fan_id: Optional[str] = None, limit: int = 10) -> List[Dict]:
        """Get recent log entries"""
        logs = []
        
        try:
            with open(self.log_file, "r") as f:
                for line in f:
                    try:
                        log_entry = json.loads(line.strip())
                        if fan_id is None or log_entry.get("fan_id") == fan_id:
                            logs.append(log_entry)
                    except json.JSONDecodeError:
                        continue
            
            return logs[-limit:] if logs else []
        except FileNotFoundError:
            return []


class ResponseFilter:
    """Filter and validate AI responses"""
    
    @staticmethod
    def check_length(response: str, max_length: int) -> bool:
        """Check if response is within length limit"""
        return len(response) <= max_length
    
    @staticmethod
    def has_inappropriate_content(response: str) -> bool:
        """
        Basic check for inappropriate content
        Note: This is a simple implementation - use a proper content moderation API in production
        """
        # This is a placeholder - implement proper content filtering
        inappropriate_keywords = [
            # Add keywords to filter if needed
        ]
        
        response_lower = response.lower()
        return any(keyword in response_lower for keyword in inappropriate_keywords)
    
    @staticmethod
    def sanitize_response(response: str, max_length: Optional[int] = None) -> str:
        """Sanitize and truncate response if needed"""
        # Remove leading/trailing whitespace
        response = response.strip()
        
        # Truncate if needed
        if max_length and len(response) > max_length:
            # Try to truncate at sentence boundary
            truncated = response[:max_length]
            last_period = truncated.rfind('.')
            last_question = truncated.rfind('?')
            last_exclamation = truncated.rfind('!')
            
            last_sentence_end = max(last_period, last_question, last_exclamation)
            
            if last_sentence_end > max_length * 0.7:  # If we can keep at least 70% of content
                response = truncated[:last_sentence_end + 1]
            else:
                response = truncated + "..."
        
        return response


class AnalyticsSummary:
    """Generate analytics summaries"""
    
    @staticmethod
    def calculate_engagement_score(
        message_count: int,
        response_rate: float,
        avg_response_time: float
    ) -> float:
        """
        Calculate engagement score (0-100)
        
        Args:
            message_count: Number of messages exchanged
            response_rate: Percentage of messages that got responses (0-1)
            avg_response_time: Average response time in seconds
            
        Returns:
            Engagement score from 0-100
        """
        # Normalize message count (cap at 100 messages)
        message_score = min(message_count / 100, 1.0) * 40
        
        # Response rate score
        response_score = response_rate * 30
        
        # Response time score (faster is better, cap at 1 hour)
        time_score = max(0, 1 - (avg_response_time / 3600)) * 30
        
        return round(message_score + response_score + time_score, 2)
    
    @staticmethod
    def calculate_revenue_potential(
        is_subscriber: bool,
        total_tips: float,
        content_purchased: int,
        message_count: int
    ) -> str:
        """
        Estimate revenue potential category
        
        Returns:
            One of: "High", "Medium", "Low"
        """
        score = 0
        
        if is_subscriber:
            score += 3
        
        if total_tips >= 100:
            score += 5
        elif total_tips >= 50:
            score += 3
        elif total_tips > 0:
            score += 1
        
        if content_purchased >= 5:
            score += 4
        elif content_purchased >= 2:
            score += 2
        elif content_purchased > 0:
            score += 1
        
        if message_count >= 50:
            score += 2
        elif message_count >= 20:
            score += 1
        
        if score >= 8:
            return "High"
        elif score >= 4:
            return "Medium"
        else:
            return "Low"


def format_price(amount: float) -> str:
    """Format price for display"""
    return f"${amount:.2f}"


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate text to maximum length"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def get_time_of_day() -> str:
    """Get current time of day"""
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"
