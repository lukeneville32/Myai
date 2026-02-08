"""
OnlyFans AI Manager - Entertainment Module
"""
from typing import List, Optional
from openai import OpenAI
from config import Config
import random


class EntertainmentManager:
    """Manages entertainment features like games, stories, and engaging content"""
    
    def __init__(self):
        """Initialize the Entertainment Manager"""
        Config.validate()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        
    def generate_flirty_game(self, fan_name: Optional[str] = None) -> str:
        """
        Generate a flirty game or challenge for fan engagement
        
        Args:
            fan_name: Optional fan name for personalization
            
        Returns:
            Game or challenge message
        """
        name = fan_name if fan_name else "you"
        
        prompt = f"""Create a fun, flirty game or challenge for a fan to play.

Examples:
- "Two truths and a lie" about yourself
- "Guess what I'm wearing" game
- "Rate my outfit" challenge
- "Caption this photo" contest
- "Would you rather" questions

Make it:
1. Fun and engaging
2. Appropriate but flirty
3. Encourages interaction
4. Personality: {", ".join(Config.MODEL_PERSONALITY)}
5. Under 200 characters

Create ONE game idea now for {name}!
"""
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are {Config.MODEL_NAME}, creating fun interactive games."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=150
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return "Let's play a game! Two truths and a lie about me - guess which is the lie! 😘"
    
    def generate_story_teaser(self, story_theme: Optional[str] = None) -> str:
        """
        Generate an engaging story teaser to build anticipation
        
        Args:
            story_theme: Optional theme for the story
            
        Returns:
            Story teaser message
        """
        theme_context = f"Theme: {story_theme}" if story_theme else "Theme: Your choice - make it intriguing"
        
        prompt = f"""Create a short, tantalizing story teaser that:

1. Hints at an interesting experience or moment
2. Creates curiosity and anticipation
3. Is {", ".join(Config.MODEL_PERSONALITY)}
4. Leaves them wanting more
5. Under 250 characters
6. Ends with intrigue

{theme_context}

Examples:
- "You won't believe what happened at the beach today... let's just say I got some interesting stares 😏"
- "Just had the most spontaneous adventure... my heart is still racing! Want to hear about it? 💕"
"""
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are {Config.MODEL_NAME}, teasing an exciting story."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=150
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return "Just had the craziest experience... you're not going to believe this! 😏✨"
    
    def generate_compliment_response(self, compliment: str) -> str:
        """
        Generate a gracious and engaging response to a compliment
        
        Args:
            compliment: The compliment received
            
        Returns:
            Response to the compliment
        """
        prompt = f"""A fan said: "{compliment}"

Generate a response that:
1. Thanks them graciously
2. Is {", ".join(Config.MODEL_PERSONALITY)}
3. Returns a subtle compliment or flirty comment
4. Keeps the conversation going
5. Under 150 characters
6. Uses emojis appropriately
"""
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are {Config.MODEL_NAME}, responding to a compliment."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=100
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return "Aww, you're so sweet! Thank you! 💕 You're making me blush!"
    
    def generate_daily_greeting(self, time_of_day: str = "morning") -> str:
        """
        Generate a personalized greeting for different times of day
        
        Args:
            time_of_day: "morning", "afternoon", "evening", or "night"
            
        Returns:
            Greeting message
        """
        prompt = f"""Generate a {time_of_day} greeting message that:

1. Is warm and welcoming
2. Matches the time of day
3. Is {", ".join(Config.MODEL_PERSONALITY)}
4. Encourages interaction
5. Under 200 characters
6. Includes emojis
7. Maybe hints at what you're up to

Make it feel personal and genuine!
"""
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are {Config.MODEL_NAME}, greeting your fans."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=120
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            greetings = {
                "morning": "Good morning! ☀️ Hope you slept well! What are you up to today?",
                "afternoon": "Hey there! 😊 How's your day going?",
                "evening": "Good evening! 🌙 How was your day?",
                "night": "Hey you! 🌙 Still up? What are you up to? 😘"
            }
            return greetings.get(time_of_day, "Hey there! 💕 How are you?")
    
    def generate_conversation_starter(self) -> str:
        """
        Generate an engaging conversation starter
        
        Returns:
            Conversation starter message
        """
        topics = [
            "Would you rather...",
            "Fun fact about me...",
            "Quick question for you...",
            "Tell me something...",
            "Let's talk about...",
            "I'm curious..."
        ]
        
        starter_type = random.choice(topics)
        
        prompt = f"""Generate a conversation starter that begins with "{starter_type}"

Make it:
1. Fun and engaging
2. {", ".join(Config.MODEL_PERSONALITY)}
3. Easy to respond to
4. Under 150 characters
5. Includes emojis
6. Shows your personality
"""
        
        try:
            response = self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are {Config.MODEL_NAME}, starting a fun conversation."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=100
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return "Quick question for you... if you could take me anywhere right now, where would we go? 🌴✨"
