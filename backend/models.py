from sqlalchemy import Column, String, Integer, Text, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class ActivityLog(Base):
    """
    Model to store user activity logs for analysis
    """
    __tablename__ = "activity_log"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), index=True)
    action = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
    context = Column(Text)
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "action": self.action,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None,
            "context": self.context
        }


class Recommendation(Base):
    """
    Model to store AI-generated recommendations
    """
    __tablename__ = "recommendations"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), index=True)
    recommendation_text = Column(Text)
    priority = Column(String(20))
    reason = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20), default="pending")  # pending, completed, dismissed
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "recommendation_text": self.recommendation_text,
            "priority": self.priority,
            "reason": self.reason,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "status": self.status
        }


# Database connection utility
def get_database_url():
    """
    Returns database URL from environment or uses SQLite for local development
    """
    import os
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        db_url = "sqlite:///./recommendation_agent.db"
    return db_url


def init_db():
    """
    Initialize database and create all tables
    """
    engine = create_engine(get_database_url())
    Base.metadata.create_all(bind=engine)
    return engine


def get_session():
    """
    Create and return a database session
    """
    engine = create_engine(get_database_url())
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()
