"""
OnlyFans AI Manager - Sales and Monetization Module
"""
from typing import Dict, List, Optional
from enum import Enum
from openai import OpenAI
from config import Config


class ContentType(Enum):
    """Types of content that can be sold"""
    PREMIUM_PHOTO = "premium_photo"
    PREMIUM_VIDEO = "premium_video"
    CUSTOM_PHOTO = "custom_photo"
    CUSTOM_VIDEO = "custom_video"
    EXCLUSIVE_MESSAGE = "exclusive_message"


class SalesManager:
    """Manages sales interactions and content suggestions"""
    
    def __init__(self):
        """Initialize the Sales Manager"""
        Config.validate()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        
    def suggest_content(
        self, 
        fan_message: str,
        fan_interests: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Analyze a fan's message and suggest appropriate content
        
        Args:
            fan_message: The fan's message
            fan_interests: Known interests of the fan
            
        Returns:
            Dictionary with content suggestions and sales pitch
        """
        interests_context = ""
        if fan_interests:
            interests_context = f"Fan's known interests: {', '.join(fan_interests)}"
        
        prompt = f"""Based on this fan's message, suggest what type of content they might be interested in purchasing:

Fan message: "{fan_message}"
{interests_context}

Analyze if they are:
1. Expressing interest in specific content
2. Making a request
3. Showing interest in custom content
4. Just chatting casually

Respond with ONLY a JSON object with these fields:
- content_type: one of [premium_photo, premium_video, custom_photo, custom_video, exclusive_message, none]
- confidence: high/medium/low
- reason: brief explanation
- suggested_pitch: a natural, flirty way to suggest this content (or empty string if none)
"""
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are a sales analysis assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=200
            )
            
            import json
            result = json.loads(response.choices[0].message.content)
            
            # Add pricing information
            if result["content_type"] in ["custom_photo", "custom_video"]:
                result["price"] = Config.CUSTOM_CONTENT_PRICE
            elif result["content_type"] != "none":
                result["price"] = Config.PREMIUM_CONTENT_PRICE
            else:
                result["price"] = 0
                
            return result
            
        except Exception as e:
            return {
                "content_type": "none",
                "confidence": "low",
                "reason": "Unable to analyze",
                "suggested_pitch": "",
                "price": 0
            }
    
    def generate_sales_response(
        self,
        fan_message: str,
        content_type: ContentType,
        custom_details: Optional[str] = None
    ) -> str:
        """
        Generate a natural sales pitch response
        
        Args:
            fan_message: The fan's message
            content_type: Type of content to pitch
            custom_details: Any custom details about the content
            
        Returns:
            Sales pitch message
        """
        price = Config.CUSTOM_CONTENT_PRICE if "custom" in content_type.value else Config.PREMIUM_CONTENT_PRICE
        
        context = f"Generate a flirty, natural response that suggests {content_type.value} content (${price})."
        if custom_details:
            context += f" Custom details: {custom_details}"
        
        prompt = f"""{context}

Fan message: "{fan_message}"

Create a response that:
1. Responds to their message warmly
2. Naturally suggests the content
3. Mentions the price casually
4. Includes a call-to-action
5. Uses appropriate emojis
6. Stays under {Config.MAX_RESPONSE_LENGTH} characters

Make it feel personal, not like a sales pitch!
"""
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system", 
                        "content": f"You are {Config.MODEL_NAME}, creating natural sales messages."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=200
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"I'd love to create something special for you! Let's chat about what you're looking for 💕"
    
    def handle_tip_thank_you(self, tip_amount: float, fan_name: Optional[str] = None) -> str:
        """
        Generate a personalized thank you message for a tip
        
        Args:
            tip_amount: Amount of the tip
            fan_name: Optional fan name
            
        Returns:
            Thank you message
        """
        name_context = f"to {fan_name}" if fan_name else ""
        
        # Determine enthusiasm level based on tip amount
        if tip_amount >= 100:
            enthusiasm = "extremely excited and grateful"
        elif tip_amount >= 50:
            enthusiasm = "very excited and appreciative"
        elif tip_amount >= 20:
            enthusiasm = "happy and thankful"
        else:
            enthusiasm = "appreciative and sweet"
        
        prompt = f"""Generate a {enthusiasm} thank you message {name_context} for a ${tip_amount} tip.

Make it:
1. Genuine and personal
2. Express appropriate excitement for the amount
3. Under 150 characters
4. Include emojis
5. Make them feel special

Be {", ".join(Config.MODEL_PERSONALITY)} in your tone.
"""
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are {Config.MODEL_NAME}, thanking a generous fan."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=100
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Thank you so much for the tip! You're amazing! 💖✨"
