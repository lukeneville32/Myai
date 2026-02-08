"""
OnlyFans AI Manager - Main API
Unified interface for all AI Manager features
"""
from typing import Dict, List, Optional
from ai_manager import AIManager
from sales_manager import SalesManager, ContentType
from entertainment_manager import EntertainmentManager
from utils import FanProfile, MessageLogger, ResponseFilter, get_time_of_day
from config import Config


class OnlyFansAIManager:
    """
    Main unified interface for the OnlyFans AI Manager
    
    This class provides a simple API for all AI manager features:
    - Fan interactions and conversations
    - Sales and monetization
    - Entertainment and engagement
    - Analytics and insights
    """
    
    def __init__(self, enable_logging: bool = True):
        """
        Initialize the OnlyFans AI Manager
        
        Args:
            enable_logging: Whether to log messages to file
        """
        Config.validate()
        
        # Initialize core managers
        self.ai_manager = AIManager()
        self.sales_manager = SalesManager()
        self.entertainment_manager = EntertainmentManager()
        
        # Initialize utilities
        self.logger = MessageLogger() if enable_logging else None
        self.response_filter = ResponseFilter()
        
        # Fan profiles storage (in-memory)
        self.fan_profiles: Dict[str, FanProfile] = {}
    
    # ===== Fan Interaction Methods =====
    
    def send_message(
        self,
        fan_id: str,
        message: str,
        auto_analyze_sales: bool = True
    ) -> Dict[str, any]:
        """
        Send a message to a fan and get AI response
        
        Args:
            fan_id: Unique identifier for the fan
            message: The fan's message
            auto_analyze_sales: Whether to automatically analyze for sales opportunities
            
        Returns:
            Dictionary with response and optional sales suggestion
        """
        # Get or create fan profile
        fan_profile = self.get_or_create_profile(fan_id)
        
        # Generate response
        response = self.ai_manager.get_response(
            fan_id,
            message,
            context=fan_profile.to_context()
        )
        
        # Sanitize response
        response = self.response_filter.sanitize_response(
            response,
            Config.MAX_RESPONSE_LENGTH
        )
        
        # Log interaction
        if self.logger:
            self.logger.log_message(fan_id, message, response, "chat")
        
        result = {
            "response": response,
            "fan_id": fan_id
        }
        
        # Optionally analyze for sales opportunities
        if auto_analyze_sales:
            sales_analysis = self.sales_manager.suggest_content(
                message,
                fan_profile.interests
            )
            
            if sales_analysis["confidence"] in ["high", "medium"]:
                result["sales_opportunity"] = sales_analysis
        
        return result
    
    def send_greeting(self, fan_id: str, custom_time: Optional[str] = None) -> str:
        """
        Send a greeting to a fan
        
        Args:
            fan_id: Unique identifier for the fan
            custom_time: Optional time of day override ("morning", "afternoon", "evening", "night")
            
        Returns:
            Greeting message
        """
        time_of_day = custom_time or get_time_of_day()
        greeting = self.entertainment_manager.generate_daily_greeting(time_of_day)
        
        if self.logger:
            self.logger.log_message(fan_id, "[greeting request]", greeting, "greeting")
        
        return greeting
    
    def get_conversation_summary(self, fan_id: str) -> Optional[str]:
        """Get a summary of conversation with a fan"""
        return self.ai_manager.get_conversation_summary(fan_id)
    
    def clear_conversation(self, fan_id: str):
        """Clear conversation history for a fan"""
        self.ai_manager.clear_conversation(fan_id)
    
    # ===== Sales Methods =====
    
    def create_sales_pitch(
        self,
        fan_id: str,
        fan_message: str,
        content_type: ContentType,
        custom_details: Optional[str] = None
    ) -> str:
        """
        Create a sales pitch for specific content
        
        Args:
            fan_id: Unique identifier for the fan
            fan_message: The fan's original message
            content_type: Type of content to pitch
            custom_details: Optional custom details
            
        Returns:
            Sales pitch message
        """
        pitch = self.sales_manager.generate_sales_response(
            fan_message,
            content_type,
            custom_details
        )
        
        if self.logger:
            self.logger.log_message(fan_id, fan_message, pitch, "sales_pitch")
        
        return pitch
    
    def thank_for_tip(
        self,
        fan_id: str,
        tip_amount: float,
        fan_name: Optional[str] = None
    ) -> str:
        """
        Generate thank you message for a tip
        
        Args:
            fan_id: Unique identifier for the fan
            tip_amount: Amount of the tip
            fan_name: Optional fan name
            
        Returns:
            Thank you message
        """
        # Update fan profile
        fan_profile = self.get_or_create_profile(fan_id)
        fan_profile.total_tips += tip_amount
        
        # Generate thank you
        thank_you = self.sales_manager.handle_tip_thank_you(tip_amount, fan_name)
        
        if self.logger:
            self.logger.log_message(
                fan_id,
                f"[tip: ${tip_amount}]",
                thank_you,
                "tip_thanks"
            )
        
        return thank_you
    
    def analyze_sales_opportunity(
        self,
        fan_message: str,
        fan_interests: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Analyze a message for sales opportunities
        
        Args:
            fan_message: The fan's message
            fan_interests: Known interests of the fan
            
        Returns:
            Sales analysis dictionary
        """
        return self.sales_manager.suggest_content(fan_message, fan_interests)
    
    # ===== Entertainment Methods =====
    
    def create_flirty_game(self, fan_id: str, fan_name: Optional[str] = None) -> str:
        """
        Create a flirty game for engagement
        
        Args:
            fan_id: Unique identifier for the fan
            fan_name: Optional fan name
            
        Returns:
            Game message
        """
        game = self.entertainment_manager.generate_flirty_game(fan_name)
        
        if self.logger:
            self.logger.log_message(fan_id, "[game request]", game, "game")
        
        return game
    
    def create_story_teaser(
        self,
        fan_id: str,
        theme: Optional[str] = None
    ) -> str:
        """
        Create a story teaser
        
        Args:
            fan_id: Unique identifier for the fan
            theme: Optional theme for the story
            
        Returns:
            Story teaser message
        """
        story = self.entertainment_manager.generate_story_teaser(theme)
        
        if self.logger:
            self.logger.log_message(fan_id, "[story request]", story, "story")
        
        return story
    
    def respond_to_compliment(self, fan_id: str, compliment: str) -> str:
        """
        Generate response to a compliment
        
        Args:
            fan_id: Unique identifier for the fan
            compliment: The compliment received
            
        Returns:
            Response message
        """
        response = self.entertainment_manager.generate_compliment_response(compliment)
        
        if self.logger:
            self.logger.log_message(fan_id, compliment, response, "compliment")
        
        return response
    
    def create_conversation_starter(self, fan_id: str) -> str:
        """
        Create a conversation starter
        
        Args:
            fan_id: Unique identifier for the fan
            
        Returns:
            Conversation starter message
        """
        starter = self.entertainment_manager.generate_conversation_starter()
        
        if self.logger:
            self.logger.log_message(fan_id, "[starter request]", starter, "starter")
        
        return starter
    
    # ===== Fan Profile Management =====
    
    def get_or_create_profile(self, fan_id: str) -> FanProfile:
        """Get or create a fan profile"""
        if fan_id not in self.fan_profiles:
            self.fan_profiles[fan_id] = FanProfile(fan_id)
        return self.fan_profiles[fan_id]
    
    def update_profile(
        self,
        fan_id: str,
        name: Optional[str] = None,
        is_subscriber: Optional[bool] = None,
        subscription_tier: Optional[str] = None,
        interests: Optional[List[str]] = None,
        notes: Optional[str] = None
    ):
        """
        Update a fan's profile
        
        Args:
            fan_id: Unique identifier for the fan
            name: Fan's name
            is_subscriber: Whether they're a subscriber
            subscription_tier: Subscription tier
            interests: List of interests
            notes: Any notes about the fan
        """
        profile = self.get_or_create_profile(fan_id)
        
        if name is not None:
            profile.name = name
        if is_subscriber is not None:
            profile.is_subscriber = is_subscriber
        if subscription_tier is not None:
            profile.subscription_tier = subscription_tier
        if interests is not None:
            profile.interests = interests
        if notes is not None:
            profile.notes = notes
    
    def record_purchase(self, fan_id: str):
        """Record that a fan purchased content"""
        profile = self.get_or_create_profile(fan_id)
        profile.content_purchased += 1
    
    def get_profile(self, fan_id: str) -> Optional[FanProfile]:
        """Get a fan's profile"""
        return self.fan_profiles.get(fan_id)
    
    # ===== Batch Operations =====
    
    def broadcast_message(self, fan_ids: List[str], message_type: str = "greeting") -> Dict[str, str]:
        """
        Send a message to multiple fans
        
        Args:
            fan_ids: List of fan IDs
            message_type: Type of message ("greeting", "starter", etc.)
            
        Returns:
            Dictionary mapping fan_id to message
        """
        results = {}
        
        for fan_id in fan_ids:
            if message_type == "greeting":
                results[fan_id] = self.send_greeting(fan_id)
            elif message_type == "starter":
                results[fan_id] = self.create_conversation_starter(fan_id)
            elif message_type == "game":
                profile = self.get_profile(fan_id)
                fan_name = profile.name if profile else None
                results[fan_id] = self.create_flirty_game(fan_id, fan_name)
        
        return results
