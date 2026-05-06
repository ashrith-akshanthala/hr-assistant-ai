from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base, TimeStampMixin


class HRKnowledge(Base, TimeStampMixin):
    __tablename__ = "hr_knowledge"

    id = Column(Integer, primary_key=True)
    category = Column(String(50), nullable=False)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
