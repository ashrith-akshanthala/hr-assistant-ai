from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base import Base, TimeStampMixin


class Employee(Base, TimeStampMixin):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)

    department = Column(String(100), nullable=False)
    role = Column(String(50), nullable=False)  # admin, manager, employee

    is_active = Column(Boolean, default=True)

    leaves = relationship(
        "Leave",
        back_populates="employee",
        foreign_keys="Leave.employee_id",
    )

    approved_leaves = relationship(
        "Leave",
        back_populates="approved_by",
        foreign_keys="Leave.approved_by_id",
    )
