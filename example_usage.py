"""
OnlyFans AI Manager - Example Usage
"""
from ai_manager import AIManager
from sales_manager import SalesManager, ContentType
from entertainment_manager import EntertainmentManager


def main():
    """Demonstrate the AI Manager capabilities"""
    
    print("=" * 60)
    print("OnlyFans AI Manager - Demo")
    print("=" * 60)
    print()
    
    # Initialize managers
    ai_manager = AIManager()
    sales_manager = SalesManager()
    entertainment_manager = EntertainmentManager()
    
    # Example 1: Basic conversation
    print("📱 Example 1: Basic Fan Interaction")
    print("-" * 60)
    fan_id = "fan_001"
    fan_message = "Hey! How are you doing today?"
    
    response = ai_manager.get_response(fan_id, fan_message)
    print(f"Fan: {fan_message}")
    print(f"You: {response}")
    print()
    
    # Example 2: Conversation with context
    print("📱 Example 2: Responding to a Subscriber")
    print("-" * 60)
    fan_id = "fan_002"
    fan_message = "I love your content! You look amazing!"
    context = {"is_subscriber": True, "has_tipped": True}
    
    response = ai_manager.get_response(fan_id, fan_message, context=context)
    print(f"Fan: {fan_message}")
    print(f"You: {response}")
    print()
    
    # Example 3: Sales suggestion
    print("💰 Example 3: Sales Content Suggestion")
    print("-" * 60)
    fan_message = "Do you have any special photos from your beach trip?"
    
    suggestion = sales_manager.suggest_content(fan_message)
    print(f"Fan: {fan_message}")
    print(f"Analysis: {suggestion}")
    
    if suggestion["content_type"] != "none":
        sales_response = sales_manager.generate_sales_response(
            fan_message,
            ContentType.PREMIUM_PHOTO
        )
        print(f"You: {sales_response}")
    print()
    
    # Example 4: Thank you for tip
    print("💝 Example 4: Thank You for Tip")
    print("-" * 60)
    tip_amount = 25.00
    thank_you = sales_manager.handle_tip_thank_you(tip_amount, "Mike")
    print(f"Fan tipped: ${tip_amount}")
    print(f"You: {thank_you}")
    print()
    
    # Example 5: Entertainment - Flirty game
    print("🎮 Example 5: Flirty Game")
    print("-" * 60)
    game = entertainment_manager.generate_flirty_game("Alex")
    print(f"You: {game}")
    print()
    
    # Example 6: Story teaser
    print("📖 Example 6: Story Teaser")
    print("-" * 60)
    story = entertainment_manager.generate_story_teaser("adventure")
    print(f"You: {story}")
    print()
    
    # Example 7: Compliment response
    print("💕 Example 7: Responding to Compliment")
    print("-" * 60)
    compliment = "You have the most beautiful smile!"
    response = entertainment_manager.generate_compliment_response(compliment)
    print(f"Fan: {compliment}")
    print(f"You: {response}")
    print()
    
    # Example 8: Daily greeting
    print("🌅 Example 8: Morning Greeting")
    print("-" * 60)
    greeting = entertainment_manager.generate_daily_greeting("morning")
    print(f"You: {greeting}")
    print()
    
    # Example 9: Conversation starter
    print("💬 Example 9: Conversation Starter")
    print("-" * 60)
    starter = entertainment_manager.generate_conversation_starter()
    print(f"You: {starter}")
    print()
    
    # Example 10: Conversation summary
    print("📝 Example 10: Conversation Summary")
    print("-" * 60)
    # Add a few messages to the conversation
    ai_manager.get_response("fan_003", "Hey, I'm new here!")
    ai_manager.get_response("fan_003", "What kind of content do you post?")
    ai_manager.get_response("fan_003", "That sounds great! I'm interested!")
    
    summary = ai_manager.get_conversation_summary("fan_003")
    print(f"Summary: {summary}")
    print()
    
    print("=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    # Note: Make sure to set OPENAI_API_KEY in .env file before running
    print("\n⚠️  IMPORTANT: Set your OPENAI_API_KEY in .env file before running!")
    print("Copy .env.example to .env and add your API key.\n")
    
    try:
        main()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("Please set up your .env file with the required configuration.")
    except Exception as e:
        print(f"❌ Error: {e}")
