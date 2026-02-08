#!/usr/bin/env python3
"""
Example scenarios demonstrating different progress states
"""

from progress_tracker import ProgressTracker


def scenario_on_track():
    """Example: Everything going well"""
    print("\n" + "="*60)
    print("SCENARIO 1: ✅ ON TRACK")
    print("="*60)
    
    tracker = ProgressTracker()
    tracker.update_content("feed_posts", 3)
    tracker.update_content("ppv_drops", 2)
    tracker.update_content("story_posts", 2)
    tracker.update_revenue(650.00)
    tracker.update_subscribers(8)
    tracker.update_customs(2)
    tracker.complete_self_check(True, True, True, True)
    
    tracker.print_status_report()


def scenario_needs_attention():
    """Example: Some areas behind"""
    print("\n" + "="*60)
    print("SCENARIO 2: 🟡 NEEDS ATTENTION")
    print("="*60)
    
    tracker = ProgressTracker()
    tracker.update_content("feed_posts", 2)
    tracker.update_content("ppv_drops", 1)
    tracker.update_content("story_posts", 1)
    tracker.update_revenue(380.00)
    tracker.update_subscribers(4)
    tracker.update_customs(1)
    tracker.complete_self_check(True, True, False, True)
    
    tracker.print_status_report()


def scenario_behind():
    """Example: Significantly behind schedule"""
    print("\n" + "="*60)
    print("SCENARIO 3: 🔴 BEHIND SCHEDULE")
    print("="*60)
    
    tracker = ProgressTracker()
    tracker.update_content("feed_posts", 1)
    tracker.update_content("ppv_drops", 0)
    tracker.update_content("story_posts", 1)
    tracker.update_revenue(150.00)
    tracker.update_subscribers(2)
    tracker.update_customs(0)
    tracker.complete_self_check(False, False, True, False)
    
    tracker.print_status_report()


def scenario_early_week():
    """Example: Early in the week"""
    print("\n" + "="*60)
    print("SCENARIO 4: 🌅 EARLY WEEK - JUST GETTING STARTED")
    print("="*60)
    
    tracker = ProgressTracker()
    tracker.update_content("feed_posts", 1)
    tracker.update_content("ppv_drops", 0)
    tracker.update_content("story_posts", 0)
    tracker.update_revenue(50.00)
    tracker.update_subscribers(1)
    
    # Self-check not completed yet
    print("\n💡 Note: Early in week, self-check pending")
    tracker.print_status_report()


if __name__ == "__main__":
    print("\n🎭 PROGRESS TRACKER - EXAMPLE SCENARIOS")
    print("="*60)
    print("Demonstrating different weekly progress states")
    
    scenario_on_track()
    input("\nPress Enter to see next scenario...")
    
    scenario_needs_attention()
    input("\nPress Enter to see next scenario...")
    
    scenario_behind()
    input("\nPress Enter to see next scenario...")
    
    scenario_early_week()
    
    print("\n" + "="*60)
    print("💡 These examples show how the tracker adapts to your progress")
    print("="*60 + "\n")
