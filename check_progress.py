#!/usr/bin/env python3
"""
Simple CLI to quickly check "Are we on track?"
"""

import sys
from progress_tracker import ProgressTracker


def quick_check():
    """Quick status check"""
    tracker = ProgressTracker()
    
    # Try to load existing data
    try:
        tracker.load_from_file("weekly_progress.json")
    except (FileNotFoundError, Exception):
        print("⚠️  No saved progress found. Please update your progress first.")
        print("Run: python progress_tracker.py")
        return
    
    # Show status report
    tracker.print_status_report()


def interactive_update():
    """Interactive mode to update progress"""
    tracker = ProgressTracker()
    
    # Try to load existing data
    try:
        tracker.load_from_file("weekly_progress.json")
        print("✅ Loaded existing progress data\n")
    except (FileNotFoundError, Exception):
        print("📝 Starting new weekly tracking\n")
    
    print("📊 UPDATE YOUR PROGRESS")
    print("="*60)
    
    # Update content
    print("\n📝 Content Creation:")
    try:
        feed = int(input("  Feed posts this week (current: {}): ".format(
            tracker.current_week_data['feed_posts'])) or tracker.current_week_data['feed_posts'])
        ppv = int(input("  PPV drops this week (current: {}): ".format(
            tracker.current_week_data['ppv_drops'])) or tracker.current_week_data['ppv_drops'])
        stories = int(input("  Story posts this week (current: {}): ".format(
            tracker.current_week_data['story_posts'])) or tracker.current_week_data['story_posts'])
        
        tracker.current_week_data['feed_posts'] = feed
        tracker.current_week_data['ppv_drops'] = ppv
        tracker.current_week_data['story_posts'] = stories
    except ValueError:
        print("⚠️  Invalid input, keeping current values")
    
    # Update revenue
    print("\n💰 Revenue & Engagement:")
    try:
        revenue = float(input("  Revenue this week ($): ") or tracker.current_week_data['revenue'])
        subs = int(input("  New subscribers: ") or tracker.current_week_data['new_subscribers'])
        customs = int(input("  Customs completed: ") or tracker.current_week_data['customs_completed'])
        
        tracker.current_week_data['revenue'] = revenue
        tracker.current_week_data['new_subscribers'] = subs
        tracker.current_week_data['customs_completed'] = customs
    except ValueError:
        print("⚠️  Invalid input, keeping current values")
    
    # Self-check
    print("\n🧘 Weekly Self-Check (y/n):")
    try:
        energy = input("  Did you protect your energy? (y/n): ").lower() == 'y'
        value = input("  Did you reinforce value? (y/n): ").lower() == 'y'
        calm = input("  Did you stay calm? (y/n): ").lower() == 'y'
        intentional = input("  Did it feel intentional? (y/n): ").lower() == 'y'
        
        tracker.complete_self_check(energy, value, calm, intentional)
    except (EOFError, KeyboardInterrupt):
        print("⚠️  Skipping self-check")
    
    # Save and show report
    tracker.save_to_file("weekly_progress.json")
    tracker.print_status_report()


def show_help():
    """Show help message"""
    print("\n🤖 MYA.MYERS PROGRESS TRACKER - CLI")
    print("="*60)
    print("\nUsage:")
    print("  python check_progress.py          - Quick status check")
    print("  python check_progress.py update   - Update progress interactively")
    print("  python check_progress.py help     - Show this help message")
    print("\nAnswers the question: 'Are we on track?'")
    print("="*60 + "\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "update":
            interactive_update()
        elif command == "help":
            show_help()
        else:
            print("⚠️  Unknown command. Use 'help' to see available commands.")
            show_help()
    else:
        quick_check()
