#!/usr/bin/env python3
"""
Progress Tracker for Mya.Myers AI Manager
Tracks content creation, revenue, and weekly goals to answer "Are we on track?"
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json


class ProgressTracker:
    """Tracks progress against weekly and monthly goals"""
    
    def __init__(self):
        self.weekly_goals = {
            "feed_posts": 3,
            "ppv_drops": 2,
            "story_posts": 1.5,  # 1-2 posts
            "rest_days": 1
        }
        
        self.current_week_data = {
            "feed_posts": 0,
            "ppv_drops": 0,
            "story_posts": 0,
            "rest_days": 0,
            "revenue": 0.0,
            "new_subscribers": 0,
            "customs_completed": 0
        }
        
        self.self_check = {
            "protected_energy": None,
            "reinforced_value": None,
            "stayed_calm": None,
            "felt_intentional": None
        }
    
    def update_content(self, content_type: str, count: int = 1):
        """Update content creation count"""
        if content_type in self.current_week_data:
            self.current_week_data[content_type] += count
    
    def update_revenue(self, amount: float):
        """Add revenue to weekly total"""
        self.current_week_data["revenue"] += amount
    
    def update_subscribers(self, count: int):
        """Update new subscriber count"""
        self.current_week_data["new_subscribers"] += count
    
    def update_customs(self, count: int):
        """Update completed customs count"""
        self.current_week_data["customs_completed"] += count
    
    def complete_self_check(self, protected_energy: bool, reinforced_value: bool,
                           stayed_calm: bool, felt_intentional: bool):
        """Complete the weekly self-check"""
        self.self_check = {
            "protected_energy": protected_energy,
            "reinforced_value": reinforced_value,
            "stayed_calm": stayed_calm,
            "felt_intentional": felt_intentional
        }
    
    def calculate_progress_percentage(self, actual: float, goal: float) -> float:
        """Calculate progress as percentage"""
        if goal == 0:
            return 100.0 if actual >= goal else 0.0
        return min((actual / goal) * 100, 100.0)
    
    def get_status_emoji(self, percentage: float) -> str:
        """Get status emoji based on progress percentage"""
        if percentage >= 100:
            return "✅"
        elif percentage >= 75:
            return "🟢"
        elif percentage >= 50:
            return "🟡"
        elif percentage >= 25:
            return "🟠"
        else:
            return "🔴"
    
    def are_we_on_track(self) -> Dict:
        """Generate comprehensive progress report"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "overall_status": "on_track",
            "content_progress": {},
            "revenue_metrics": {},
            "self_check_status": "pending",
            "recommendations": []
        }
        
        # Content Progress
        content_items = ["feed_posts", "ppv_drops", "story_posts"]
        on_track_count = 0
        total_items = len(content_items)
        
        for item in content_items:
            actual = self.current_week_data[item]
            goal = self.weekly_goals[item]
            percentage = self.calculate_progress_percentage(actual, goal)
            status = self.get_status_emoji(percentage)
            
            report["content_progress"][item] = {
                "actual": actual,
                "goal": goal,
                "percentage": round(percentage, 1),
                "status": status
            }
            
            if percentage >= 75:
                on_track_count += 1
            elif percentage < 50:
                report["recommendations"].append(
                    f"⚠️  {item.replace('_', ' ').title()}: Behind schedule ({actual}/{goal})"
                )
        
        # Revenue Metrics
        report["revenue_metrics"] = {
            "weekly_revenue": self.current_week_data["revenue"],
            "new_subscribers": self.current_week_data["new_subscribers"],
            "customs_completed": self.current_week_data["customs_completed"]
        }
        
        # Self-Check Status
        if all(v is True for v in self.self_check.values() if v is not None):
            report["self_check_status"] = "✅ Excellent - All checks passed"
        elif any(v is False for v in self.self_check.values()):
            report["self_check_status"] = "⚠️  Needs attention"
            failed_checks = [k for k, v in self.self_check.items() if v is False]
            report["recommendations"].append(
                f"Self-check concerns: {', '.join(failed_checks)}"
            )
        else:
            report["self_check_status"] = "⏳ Pending completion"
        
        # Overall Status Determination
        # Calculate average progress across all content items
        avg_progress = sum(
            report["content_progress"][item]["percentage"] 
            for item in content_items
        ) / total_items
        
        if avg_progress >= 75 and report["self_check_status"] == "✅ Excellent - All checks passed":
            report["overall_status"] = "✅ ON TRACK"
        elif avg_progress >= 60 or report["self_check_status"] == "✅ Excellent - All checks passed":
            report["overall_status"] = "🟡 NEEDS ATTENTION"
        else:
            report["overall_status"] = "🔴 BEHIND SCHEDULE"
        
        return report
    
    def print_status_report(self):
        """Print a formatted status report"""
        report = self.are_we_on_track()
        
        print("\n" + "="*60)
        print("📊 MYA.MYERS PROGRESS TRACKER")
        print("="*60)
        print(f"\n⏰ Report Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"\n🎯 Overall Status: {report['overall_status']}")
        
        print("\n" + "-"*60)
        print("📝 CONTENT CREATION PROGRESS")
        print("-"*60)
        
        for item, data in report['content_progress'].items():
            item_name = item.replace('_', ' ').title()
            print(f"{data['status']} {item_name}: {data['actual']}/{data['goal']} "
                  f"({data['percentage']}%)")
        
        print("\n" + "-"*60)
        print("💰 REVENUE & ENGAGEMENT METRICS")
        print("-"*60)
        metrics = report['revenue_metrics']
        print(f"💵 Weekly Revenue: ${metrics['weekly_revenue']:.2f}")
        print(f"👥 New Subscribers: {metrics['new_subscribers']}")
        print(f"🎨 Customs Completed: {metrics['customs_completed']}")
        
        print("\n" + "-"*60)
        print("🧘 WEEKLY SELF-CHECK")
        print("-"*60)
        print(f"Status: {report['self_check_status']}")
        
        if self.self_check['protected_energy'] is not None:
            for key, value in self.self_check.items():
                check_name = key.replace('_', ' ').title()
                status = "✅" if value else "❌"
                print(f"  {status} {check_name}")
        
        if report['recommendations']:
            print("\n" + "-"*60)
            print("💡 RECOMMENDATIONS")
            print("-"*60)
            for rec in report['recommendations']:
                print(f"  {rec}")
        
        print("\n" + "="*60 + "\n")
    
    def save_to_file(self, filename: str = "weekly_progress.json"):
        """Save current progress to JSON file"""
        data = {
            "timestamp": datetime.now().isoformat(),
            "weekly_data": self.current_week_data,
            "self_check": self.self_check,
            "report": self.are_we_on_track()
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Progress saved to {filename}")
    
    def load_from_file(self, filename: str = "weekly_progress.json"):
        """Load progress from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.current_week_data = data['weekly_data']
                self.self_check = data['self_check']
            print(f"✅ Progress loaded from {filename}")
        except FileNotFoundError:
            print(f"⚠️  File {filename} not found. Starting fresh.")


def main():
    """Example usage and demonstration"""
    tracker = ProgressTracker()
    
    print("\n🤖 Welcome to Mya.Myers AI Manager - Progress Tracker")
    print("="*60)
    
    # Example: Add some sample data
    print("\n📝 Adding sample weekly data...")
    tracker.update_content("feed_posts", 2)
    tracker.update_content("ppv_drops", 1)
    tracker.update_content("story_posts", 2)
    tracker.update_revenue(450.00)
    tracker.update_subscribers(5)
    tracker.update_customs(1)
    
    # Complete self-check
    print("🧘 Completing weekly self-check...")
    tracker.complete_self_check(
        protected_energy=True,
        reinforced_value=True,
        stayed_calm=True,
        felt_intentional=True
    )
    
    # Generate and print report
    print("\n📊 Generating progress report...")
    tracker.print_status_report()
    
    # Save to file
    tracker.save_to_file("weekly_progress.json")
    
    print("\n✨ To check if you're on track, run this script anytime!")
    print("💡 Update your progress regularly for accurate tracking.")


if __name__ == "__main__":
    main()
