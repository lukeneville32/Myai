#!/usr/bin/env python3
"""
Comprehensive test of the progress tracking system
"""

from progress_tracker import ProgressTracker
import os
import json


def test_basic_functionality():
    """Test basic tracking operations"""
    print("Testing basic functionality...")
    
    tracker = ProgressTracker()
    
    # Test content updates
    tracker.update_content("feed_posts", 2)
    assert tracker.current_week_data["feed_posts"] == 2
    
    tracker.update_content("ppv_drops", 1)
    assert tracker.current_week_data["ppv_drops"] == 1
    
    # Test revenue update
    tracker.update_revenue(100.50)
    assert tracker.current_week_data["revenue"] == 100.50
    
    # Test subscribers update
    tracker.update_subscribers(5)
    assert tracker.current_week_data["new_subscribers"] == 5
    
    print("✅ Basic functionality test passed")


def test_self_check():
    """Test self-check functionality"""
    print("Testing self-check...")
    
    tracker = ProgressTracker()
    tracker.complete_self_check(True, True, False, True)
    
    assert tracker.self_check["protected_energy"] == True
    assert tracker.self_check["stayed_calm"] == False
    
    print("✅ Self-check test passed")


def test_progress_calculation():
    """Test progress percentage calculation"""
    print("Testing progress calculations...")
    
    tracker = ProgressTracker()
    
    # Test 100% progress
    percentage = tracker.calculate_progress_percentage(3, 3)
    assert percentage == 100.0
    
    # Test 50% progress
    percentage = tracker.calculate_progress_percentage(1, 2)
    assert percentage == 50.0
    
    # Test over 100% (should cap at 100)
    percentage = tracker.calculate_progress_percentage(5, 3)
    assert percentage == 100.0
    
    print("✅ Progress calculation test passed")


def test_status_report():
    """Test status report generation"""
    print("Testing status report generation...")
    
    tracker = ProgressTracker()
    tracker.update_content("feed_posts", 3)
    tracker.update_content("ppv_drops", 2)
    tracker.update_content("story_posts", 2)
    tracker.complete_self_check(True, True, True, True)
    
    report = tracker.are_we_on_track()
    
    assert "content_progress" in report
    assert "revenue_metrics" in report
    assert "self_check_status" in report
    assert "overall_status" in report
    
    # Should be on track with all goals met
    assert report["overall_status"] == "✅ ON TRACK"
    
    print("✅ Status report test passed")


def test_file_operations():
    """Test save/load functionality"""
    print("Testing file operations...")
    
    test_file = "test_progress.json"
    
    # Create and save tracker
    tracker1 = ProgressTracker()
    tracker1.update_content("feed_posts", 2)
    tracker1.update_revenue(250.00)
    tracker1.save_to_file(test_file)
    
    # Load into new tracker
    tracker2 = ProgressTracker()
    tracker2.load_from_file(test_file)
    
    assert tracker2.current_week_data["feed_posts"] == 2
    assert tracker2.current_week_data["revenue"] == 250.00
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("✅ File operations test passed")


def test_status_emojis():
    """Test status emoji assignment"""
    print("Testing status emojis...")
    
    tracker = ProgressTracker()
    
    assert tracker.get_status_emoji(100) == "✅"
    assert tracker.get_status_emoji(80) == "🟢"
    assert tracker.get_status_emoji(60) == "🟡"
    assert tracker.get_status_emoji(40) == "🟠"
    assert tracker.get_status_emoji(20) == "🔴"
    
    print("✅ Status emoji test passed")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("🧪 RUNNING PROGRESS TRACKER TESTS")
    print("="*60 + "\n")
    
    test_basic_functionality()
    test_self_check()
    test_progress_calculation()
    test_status_report()
    test_file_operations()
    test_status_emojis()
    
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED!")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_all_tests()
