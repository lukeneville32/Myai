"""
OnlyFans AI Manager - Simple API Usage Example
Demonstrates using the unified OnlyFansAIManager API
"""
from onlyfans_ai import OnlyFansAIManager
from sales_manager import ContentType


def main():
    """Demonstrate simple usage of the unified API"""
    
    print("=" * 70)
    print("OnlyFans AI Manager - Simple API Usage")
    print("=" * 70)
    print()
    
    # Initialize the AI Manager
    print("🚀 Initializing AI Manager...")
    ai = OnlyFansAIManager(enable_logging=True)
    print("✅ Ready!\n")
    
    # Example 1: Update fan profile
    print("👤 Example 1: Setting up fan profile")
    print("-" * 70)
    ai.update_profile(
        fan_id="fan_john",
        name="John",
        is_subscriber=True,
        interests=["fitness", "travel"]
    )
    print("✅ Profile created for John\n")
    
    # Example 2: Simple message exchange
    print("💬 Example 2: Message exchange")
    print("-" * 70)
    result = ai.send_message(
        fan_id="fan_john",
        message="Hey! How was your day?"
    )
    print(f"Fan: Hey! How was your day?")
    print(f"You: {result['response']}")
    
    if "sales_opportunity" in result:
        print(f"\n💡 Sales Opportunity Detected:")
        print(f"   Type: {result['sales_opportunity']['content_type']}")
        print(f"   Confidence: {result['sales_opportunity']['confidence']}")
    print()
    
    # Example 3: Responding to content request
    print("💬 Example 3: Content request")
    print("-" * 70)
    result = ai.send_message(
        fan_id="fan_john",
        message="Do you have any photos from your gym session?"
    )
    print(f"Fan: Do you have any photos from your gym session?")
    print(f"You: {result['response']}")
    
    if "sales_opportunity" in result:
        print(f"\n💡 Sales Opportunity:")
        print(f"   {result['sales_opportunity']['suggested_pitch']}")
    print()
    
    # Example 4: Thank you for tip
    print("💝 Example 4: Thank you for tip")
    print("-" * 70)
    thank_you = ai.thank_for_tip(
        fan_id="fan_john",
        tip_amount=20.00,
        fan_name="John"
    )
    print(f"Fan tipped: $20.00")
    print(f"You: {thank_you}\n")
    
    # Example 5: Create a sales pitch
    print("💰 Example 5: Direct sales pitch")
    print("-" * 70)
    pitch = ai.create_sales_pitch(
        fan_id="fan_john",
        fan_message="I'd love to see more exclusive content",
        content_type=ContentType.PREMIUM_VIDEO,
        custom_details="Behind the scenes gym workout"
    )
    print(f"Fan: I'd love to see more exclusive content")
    print(f"You: {pitch}\n")
    
    # Example 6: Entertainment - Flirty game
    print("🎮 Example 6: Flirty game")
    print("-" * 70)
    game = ai.create_flirty_game(fan_id="fan_john", fan_name="John")
    print(f"You: {game}\n")
    
    # Example 7: Story teaser
    print("📖 Example 7: Story teaser")
    print("-" * 70)
    story = ai.create_story_teaser(fan_id="fan_john", theme="beach adventure")
    print(f"You: {story}\n")
    
    # Example 8: Respond to compliment
    print("💕 Example 8: Compliment response")
    print("-" * 70)
    response = ai.respond_to_compliment(
        fan_id="fan_john",
        compliment="You look absolutely stunning in that dress!"
    )
    print(f"Fan: You look absolutely stunning in that dress!")
    print(f"You: {response}\n")
    
    # Example 9: Send greeting
    print("🌅 Example 9: Morning greeting")
    print("-" * 70)
    greeting = ai.send_greeting(fan_id="fan_john", custom_time="morning")
    print(f"You: {greeting}\n")
    
    # Example 10: Conversation starter
    print("💬 Example 10: Conversation starter")
    print("-" * 70)
    starter = ai.create_conversation_starter(fan_id="fan_john")
    print(f"You: {starter}\n")
    
    # Example 11: Get conversation summary
    print("📊 Example 11: Conversation summary")
    print("-" * 70)
    summary = ai.get_conversation_summary("fan_john")
    if summary:
        print(f"Summary: {summary}")
    else:
        print("No conversation history")
    print()
    
    # Example 12: Batch operations
    print("📢 Example 12: Broadcast greeting to multiple fans")
    print("-" * 70)
    fan_ids = ["fan_sarah", "fan_mike", "fan_alex"]
    results = ai.broadcast_message(fan_ids, message_type="greeting")
    
    for fan_id, message in results.items():
        print(f"{fan_id}: {message}")
    print()
    
    # Example 13: Check fan profile
    print("👤 Example 13: View fan profile")
    print("-" * 70)
    profile = ai.get_profile("fan_john")
    if profile:
        print(f"Fan: {profile.name}")
        print(f"Subscriber: {profile.is_subscriber}")
        print(f"Total Tips: ${profile.total_tips:.2f}")
        print(f"Content Purchased: {profile.content_purchased}")
        print(f"Interests: {', '.join(profile.interests)}")
    print()
    
    print("=" * 70)
    print("✅ Demo Complete!")
    print("=" * 70)
    print("\n💡 Tips:")
    print("   - All interactions are automatically logged to messages.log")
    print("   - Sales opportunities are automatically detected")
    print("   - Fan profiles track engagement and purchases")
    print("   - Conversation context is maintained across messages")


if __name__ == "__main__":
    print("\n⚠️  IMPORTANT: Set your OPENAI_API_KEY in .env file before running!")
    print("Copy .env.example to .env and add your API key.\n")
    
    try:
        main()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("Please set up your .env file with the required configuration.")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
