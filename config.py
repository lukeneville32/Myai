"""
OnlyFans AI Manager - Configuration Module
"""
import os
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class for the AI Manager"""
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Model Settings
    MODEL_NAME: str = os.getenv("MODEL_NAME", "Your Name")
    MODEL_PERSONALITY: List[str] = os.getenv("MODEL_PERSONALITY", "flirty,playful,engaging").split(",")
    MODEL_INTERESTS: List[str] = os.getenv("MODEL_INTERESTS", "fitness,travel,photography").split(",")
    
    # Sales Settings
    PREMIUM_CONTENT_PRICE: float = float(os.getenv("PREMIUM_CONTENT_PRICE", "9.99"))
    CUSTOM_CONTENT_PRICE: float = float(os.getenv("CUSTOM_CONTENT_PRICE", "29.99"))
    TIP_MINIMUM: float = float(os.getenv("TIP_MINIMUM", "5.00"))
    
    # Response Settings
    MAX_RESPONSE_LENGTH: int = int(os.getenv("MAX_RESPONSE_LENGTH", "500"))
    RESPONSE_TEMPERATURE: float = float(os.getenv("RESPONSE_TEMPERATURE", "0.8"))
    
    # OpenAI Model
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4")
    
    @classmethod
    def validate(cls) -> bool:
        """Validate that required configuration is set"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY must be set in environment variables")
        return True
