"""
OnlyFans AI Manager - Core AI Module
"""
from typing import Dict, List, Optional
from openai import OpenAI
from config import Config


class AIManager:
    """Main AI Manager for handling fan interactions"""
    
    def __init__(self):
        """Initialize the AI Manager"""
        Config.validate()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.conversation_history: Dict[str, List[Dict]] = {}
        
    def _get_system_prompt(self) -> str:
        """Generate the system prompt based on configuration"""
        personality_traits = ", ".join(Config.MODEL_PERSONALITY)
        interests = ", ".join(Config.MODEL_INTERESTS)
        
        return f"""You are {Config.MODEL_NAME}, an OnlyFans content creator. Your personality is {personality_traits}.

Your interests include: {interests}.

Your role is to:
1. Engage with fans in a friendly, flirty, and entertaining way
2. Build genuine connections while maintaining appropriate boundaries
3. Suggest premium content and custom requests when appropriate
4. Keep responses under {Config.MAX_RESPONSE_LENGTH} characters
5. Be authentic and match the fan's energy level

Pricing information:
- Premium content: ${Config.PREMIUM_CONTENT_PRICE}
- Custom content requests: ${Config.CUSTOM_CONTENT_PRICE}
- Minimum tip: ${Config.TIP_MINIMUM}

Guidelines:
- Always be respectful and professional
- Don't be pushy about sales - be natural
- Show genuine interest in your fans
- Use emojis appropriately to convey emotion
- Keep things fun and engaging
- Respond to compliments graciously
- When fans ask for content, suggest premium options naturally
"""

    def get_response(
        self, 
        fan_id: str, 
        message: str,
        context: Optional[Dict] = None
    ) -> str:
        """
        Generate a response to a fan's message
        
        Args:
            fan_id: Unique identifier for the fan
            message: The fan's message
            context: Optional context about the interaction (e.g., has_subscribed, tip_history)
            
        Returns:
            AI-generated response
        """
        # Initialize conversation history for new fans
        if fan_id not in self.conversation_history:
            self.conversation_history[fan_id] = []
        
        # Add context to the message if provided
        enhanced_message = message
        if context:
            context_info = []
            if context.get("is_subscriber"):
                context_info.append("(This fan is a subscriber)")
            if context.get("has_tipped"):
                context_info.append("(This fan has tipped before)")
            if context.get("purchased_content"):
                context_info.append("(This fan has purchased content)")
            
            if context_info:
                enhanced_message = f"{message} {' '.join(context_info)}"
        
        # Add user message to history
        self.conversation_history[fan_id].append({
            "role": "user",
            "content": enhanced_message
        })
        
        # Keep only last 10 messages to manage token usage
        if len(self.conversation_history[fan_id]) > 10:
            self.conversation_history[fan_id] = self.conversation_history[fan_id][-10:]
        
        # Generate response
        messages = [
            {"role": "system", "content": self._get_system_prompt()}
        ] + self.conversation_history[fan_id]
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=messages,
                temperature=Config.RESPONSE_TEMPERATURE,
                max_tokens=300
            )
            
            ai_response = response.choices[0].message.content
            
            # Add AI response to history
            self.conversation_history[fan_id].append({
                "role": "assistant",
                "content": ai_response
            })
            
            return ai_response
            
        except Exception as e:
            return f"I'm having trouble responding right now, but I'll get back to you soon! 💕"
    
    def clear_conversation(self, fan_id: str) -> None:
        """Clear conversation history for a specific fan"""
        if fan_id in self.conversation_history:
            del self.conversation_history[fan_id]
    
    def get_conversation_summary(self, fan_id: str) -> Optional[str]:
        """Get a summary of the conversation with a fan"""
        if fan_id not in self.conversation_history or not self.conversation_history[fan_id]:
            return None
        
        messages = self.conversation_history[fan_id]
        conversation_text = "\n".join([
            f"{'Fan' if msg['role'] == 'user' else 'You'}: {msg['content']}"
            for msg in messages
        ])
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": "Summarize this conversation in 2-3 sentences, focusing on key topics and the fan's interests."
                    },
                    {
                        "role": "user",
                        "content": conversation_text
                    }
                ],
                temperature=0.5,
                max_tokens=150
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return "Unable to generate summary at this time."
