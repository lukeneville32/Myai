"""
OnlyFans AI Manager - Interactive Demo
Run this script to interact with the AI Manager in real-time
"""
from ai_manager import AIManager
from sales_manager import SalesManager, ContentType
from entertainment_manager import EntertainmentManager
from config import Config
import sys


class InteractiveDemo:
    """Interactive demo for testing the AI Manager"""
    
    def __init__(self):
        """Initialize the demo"""
        try:
            Config.validate()
            self.ai_manager = AIManager()
            self.sales_manager = SalesManager()
            self.entertainment_manager = EntertainmentManager()
            self.current_fan_id = "demo_fan"
            self.running = True
            print("✅ AI Manager initialized successfully!")
        except ValueError as e:
            print(f"❌ Configuration Error: {e}")
            print("Please set up your .env file with OPENAI_API_KEY")
            sys.exit(1)
    
    def print_menu(self):
        """Print the interactive menu"""
        print("\n" + "=" * 60)
        print("OnlyFans AI Manager - Interactive Demo")
        print("=" * 60)
        print("\n📱 Chat Options:")
        print("  1. Send a message as a fan")
        print("  2. Get conversation summary")
        print("  3. Clear conversation history")
        print("\n💰 Sales Options:")
        print("  4. Analyze message for sales opportunity")
        print("  5. Generate sales pitch")
        print("  6. Thank you for tip")
        print("\n🎮 Entertainment Options:")
        print("  7. Generate flirty game")
        print("  8. Create story teaser")
        print("  9. Respond to compliment")
        print("  10. Daily greeting")
        print("  11. Conversation starter")
        print("\n⚙️  Settings:")
        print("  12. Change fan ID")
        print("  13. View current configuration")
        print("\n  0. Exit")
        print("=" * 60)
    
    def handle_chat_message(self):
        """Handle sending a chat message"""
        print("\n💬 Fan Message:")
        message = input("Enter message: ").strip()
        
        if not message:
            print("❌ Message cannot be empty")
            return
        
        print("\n📝 Options:")
        print("  1. Regular fan")
        print("  2. Subscriber")
        print("  3. Subscriber who has tipped")
        choice = input("Select fan type (1-3, default 1): ").strip() or "1"
        
        context = {}
        if choice == "2":
            context = {"is_subscriber": True}
        elif choice == "3":
            context = {"is_subscriber": True, "has_tipped": True}
        
        print(f"\n🤖 Generating response...")
        response = self.ai_manager.get_response(
            self.current_fan_id,
            message,
            context=context
        )
        
        print(f"\n✨ Your Response:")
        print(f"{response}")
    
    def handle_conversation_summary(self):
        """Get conversation summary"""
        print(f"\n📊 Getting conversation summary for {self.current_fan_id}...")
        summary = self.ai_manager.get_conversation_summary(self.current_fan_id)
        
        if summary:
            print(f"\n✨ Summary:")
            print(f"{summary}")
        else:
            print("❌ No conversation history found")
    
    def handle_clear_history(self):
        """Clear conversation history"""
        self.ai_manager.clear_conversation(self.current_fan_id)
        print(f"\n✅ Conversation history cleared for {self.current_fan_id}")
    
    def handle_sales_analysis(self):
        """Analyze message for sales opportunity"""
        print("\n💰 Sales Analysis:")
        message = input("Enter fan message: ").strip()
        
        if not message:
            print("❌ Message cannot be empty")
            return
        
        print("\n🤖 Analyzing...")
        suggestion = self.sales_manager.suggest_content(message)
        
        print(f"\n✨ Analysis Results:")
        print(f"Content Type: {suggestion['content_type']}")
        print(f"Confidence: {suggestion['confidence']}")
        print(f"Reason: {suggestion['reason']}")
        if suggestion['suggested_pitch']:
            print(f"Suggested Pitch: {suggestion['suggested_pitch']}")
        if suggestion['price'] > 0:
            print(f"Price: ${suggestion['price']}")
    
    def handle_sales_pitch(self):
        """Generate a sales pitch"""
        print("\n💰 Generate Sales Pitch:")
        message = input("Enter fan message: ").strip()
        
        if not message:
            print("❌ Message cannot be empty")
            return
        
        print("\n📝 Content Types:")
        print("  1. Premium Photo")
        print("  2. Premium Video")
        print("  3. Custom Photo")
        print("  4. Custom Video")
        choice = input("Select content type (1-4): ").strip()
        
        content_type_map = {
            "1": ContentType.PREMIUM_PHOTO,
            "2": ContentType.PREMIUM_VIDEO,
            "3": ContentType.CUSTOM_PHOTO,
            "4": ContentType.CUSTOM_VIDEO
        }
        
        content_type = content_type_map.get(choice, ContentType.PREMIUM_PHOTO)
        
        print("\n🤖 Generating sales pitch...")
        pitch = self.sales_manager.generate_sales_response(message, content_type)
        
        print(f"\n✨ Sales Pitch:")
        print(f"{pitch}")
    
    def handle_tip_thanks(self):
        """Generate thank you for tip"""
        print("\n💝 Thank You for Tip:")
        
        try:
            amount = float(input("Enter tip amount ($): ").strip())
            name = input("Fan name (optional, press Enter to skip): ").strip() or None
            
            print("\n🤖 Generating thank you message...")
            message = self.sales_manager.handle_tip_thank_you(amount, name)
            
            print(f"\n✨ Thank You Message:")
            print(f"{message}")
        except ValueError:
            print("❌ Invalid amount")
    
    def handle_flirty_game(self):
        """Generate a flirty game"""
        print("\n🎮 Generate Flirty Game:")
        name = input("Fan name (optional, press Enter to skip): ").strip() or None
        
        print("\n🤖 Creating game...")
        game = self.entertainment_manager.generate_flirty_game(name)
        
        print(f"\n✨ Game:")
        print(f"{game}")
    
    def handle_story_teaser(self):
        """Generate a story teaser"""
        print("\n📖 Generate Story Teaser:")
        theme = input("Theme (optional, press Enter for random): ").strip() or None
        
        print("\n🤖 Creating story...")
        story = self.entertainment_manager.generate_story_teaser(theme)
        
        print(f"\n✨ Story Teaser:")
        print(f"{story}")
    
    def handle_compliment_response(self):
        """Generate compliment response"""
        print("\n💕 Respond to Compliment:")
        compliment = input("Enter compliment: ").strip()
        
        if not compliment:
            print("❌ Compliment cannot be empty")
            return
        
        print("\n🤖 Generating response...")
        response = self.entertainment_manager.generate_compliment_response(compliment)
        
        print(f"\n✨ Your Response:")
        print(f"{response}")
    
    def handle_daily_greeting(self):
        """Generate daily greeting"""
        print("\n🌅 Generate Daily Greeting:")
        print("  1. Morning")
        print("  2. Afternoon")
        print("  3. Evening")
        print("  4. Night")
        choice = input("Select time of day (1-4): ").strip()
        
        time_map = {
            "1": "morning",
            "2": "afternoon",
            "3": "evening",
            "4": "night"
        }
        
        time_of_day = time_map.get(choice, "morning")
        
        print("\n🤖 Creating greeting...")
        greeting = self.entertainment_manager.generate_daily_greeting(time_of_day)
        
        print(f"\n✨ Greeting:")
        print(f"{greeting}")
    
    def handle_conversation_starter(self):
        """Generate conversation starter"""
        print("\n💬 Generate Conversation Starter:")
        print("\n🤖 Creating starter...")
        starter = self.entertainment_manager.generate_conversation_starter()
        
        print(f"\n✨ Conversation Starter:")
        print(f"{starter}")
    
    def handle_change_fan_id(self):
        """Change the current fan ID"""
        print(f"\n⚙️  Current Fan ID: {self.current_fan_id}")
        new_id = input("Enter new fan ID: ").strip()
        
        if new_id:
            self.current_fan_id = new_id
            print(f"✅ Fan ID changed to: {self.current_fan_id}")
        else:
            print("❌ Fan ID cannot be empty")
    
    def handle_view_config(self):
        """View current configuration"""
        print("\n⚙️  Current Configuration:")
        print(f"Model Name: {Config.MODEL_NAME}")
        print(f"Personality: {', '.join(Config.MODEL_PERSONALITY)}")
        print(f"Interests: {', '.join(Config.MODEL_INTERESTS)}")
        print(f"Premium Content Price: ${Config.PREMIUM_CONTENT_PRICE}")
        print(f"Custom Content Price: ${Config.CUSTOM_CONTENT_PRICE}")
        print(f"Tip Minimum: ${Config.TIP_MINIMUM}")
        print(f"OpenAI Model: {Config.OPENAI_MODEL}")
    
    def run(self):
        """Run the interactive demo"""
        print("\n🎉 Welcome to the OnlyFans AI Manager Interactive Demo!")
        
        while self.running:
            self.print_menu()
            choice = input("\nSelect an option: ").strip()
            
            try:
                if choice == "0":
                    print("\n👋 Thanks for using the AI Manager! Goodbye!")
                    self.running = False
                elif choice == "1":
                    self.handle_chat_message()
                elif choice == "2":
                    self.handle_conversation_summary()
                elif choice == "3":
                    self.handle_clear_history()
                elif choice == "4":
                    self.handle_sales_analysis()
                elif choice == "5":
                    self.handle_sales_pitch()
                elif choice == "6":
                    self.handle_tip_thanks()
                elif choice == "7":
                    self.handle_flirty_game()
                elif choice == "8":
                    self.handle_story_teaser()
                elif choice == "9":
                    self.handle_compliment_response()
                elif choice == "10":
                    self.handle_daily_greeting()
                elif choice == "11":
                    self.handle_conversation_starter()
                elif choice == "12":
                    self.handle_change_fan_id()
                elif choice == "13":
                    self.handle_view_config()
                else:
                    print("❌ Invalid option. Please try again.")
                
                if choice != "0":
                    input("\nPress Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Thanks for using the AI Manager! Goodbye!")
                self.running = False
            except Exception as e:
                print(f"\n❌ Error: {e}")
                input("\nPress Enter to continue...")


if __name__ == "__main__":
    demo = InteractiveDemo()
    demo.run()
