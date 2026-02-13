"""
Sample data seeder for testing the recommendation system
Generates realistic activity logs for demo users
"""
from models import ActivityLog, init_db, get_session
from datetime import datetime, timedelta
import random

# Sample data for different user scenarios
SAMPLE_ACTIVITIES = {
    "sales_rep": [
        ("email_opened", "Q1 campaign - Lead ABC Corp"),
        ("email_opened", "Follow-up - ABC Corp"),
        ("call_scheduled", "Demo call with ABC Corp"),
        ("email_sent", "Proposal sent to ABC Corp"),
        ("email_opened", "Q1 campaign - Lead XYZ Inc"),
        ("meeting_attended", "Sales team weekly sync"),
        ("crm_updated", "Added notes for ABC Corp"),
        ("email_opened", "Q1 campaign - Lead DEF Ltd"),
        ("call_completed", "Discovery call with XYZ Inc"),
        ("email_sent", "Follow-up email to XYZ Inc"),
    ],
    "customer_success": [
        ("ticket_viewed", "Support ticket #123 - Bug report"),
        ("ticket_viewed", "Support ticket #124 - Feature request"),
        ("customer_call", "Check-in call with Acme Inc"),
        ("ticket_resolved", "Support ticket #123"),
        ("email_sent", "Product update notification"),
        ("ticket_viewed", "Support ticket #125 - Integration issue"),
        ("documentation_updated", "Updated API docs"),
        ("ticket_viewed", "Support ticket #126 - Billing question"),
        ("customer_call", "Onboarding call with Beta Corp"),
        ("health_score_check", "Reviewed customer health metrics"),
    ],
    "product_manager": [
        ("feature_request_reviewed", "Mobile app improvement"),
        ("user_feedback_analyzed", "Q4 survey results"),
        ("roadmap_updated", "Added Q2 priorities"),
        ("meeting_attended", "Product strategy session"),
        ("analytics_reviewed", "User engagement metrics"),
        ("competitor_research", "Analyzed competitor feature set"),
        ("feature_request_reviewed", "API enhancement request"),
        ("user_interview", "Interview with enterprise customer"),
        ("sprint_planning", "Sprint 12 planning"),
        ("feature_request_reviewed", "Dashboard customization"),
    ]
}


def seed_sample_data():
    """
    Seed database with sample activity logs
    """
    print("🌱 Seeding sample data...")
    
    # Initialize database
    init_db()
    db = get_session()
    
    try:
        # Clear existing data
        db.query(ActivityLog).delete()
        db.commit()
        print("✓ Cleared existing data")
        
        # Create activities for each user type
        base_time = datetime.utcnow()
        
        for user_type, activities in SAMPLE_ACTIVITIES.items():
            user_id = f"{user_type}_001"
            print(f"\n👤 Creating activities for {user_id}...")
            
            for i, (action, context) in enumerate(activities):
                # Create timestamps going back in time
                timestamp = base_time - timedelta(hours=len(activities) - i)
                
                log = ActivityLog(
                    user_id=user_id,
                    action=action,
                    context=context,
                    timestamp=timestamp
                )
                db.add(log)
                print(f"  ✓ {action}")
            
            db.commit()
            print(f"✅ Created {len(activities)} activities for {user_id}")
        
        # Display summary
        total_count = db.query(ActivityLog).count()
        print(f"\n🎉 Successfully seeded {total_count} activity logs!")
        print("\n📊 Test users created:")
        for user_type in SAMPLE_ACTIVITIES.keys():
            print(f"  - {user_type}_001")
        
        print("\n🚀 You can now test with these user IDs!")
        
    except Exception as e:
        print(f"❌ Error seeding data: {str(e)}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_sample_data()
