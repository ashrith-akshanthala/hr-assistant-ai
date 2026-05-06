from datetime import datetime, timezone

from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    started_at = Column(DateTime, default=datetime.now(timezone.utc))
    context = Column(JSON, default=dict)

    employee = relationship("Employee")
    messages = relationship("ChatMessage", back_populates="session")


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"))

    sender = Column(String(10), nullable=False)  # user | bot
    message = Column(Text, nullable=False)

    intent = Column(String(100), nullable=True)
    confidence = Column(Integer, nullable=True)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    session = relationship("ChatSession", back_populates="messages")
