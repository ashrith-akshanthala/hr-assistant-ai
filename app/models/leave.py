import enum

from sqlalchemy import Column, Date, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base, TimeStampMixin


class LeaveStatus(enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


class Leave(Base, TimeStampMixin):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    approved_by_id = Column(Integer, ForeignKey("employees.id"), nullable=True)

    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    leave_type = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)

    status = Column(
        Enum(LeaveStatus),
        default=LeaveStatus.PENDING,
        nullable=False,
    )

    reject_reason = Column(String(150), nullable=True)

    employee = relationship(
        "Employee",
        foreign_keys=[employee_id],
        back_populates="leaves",
    )

    approved_by = relationship(
        "Employee",
        foreign_keys=[approved_by_id],
        back_populates="approved_leaves",
    )


class LeaveBalance(Base, TimeStampMixin):
    __tablename__ = "leave_balances"

    id = Column(Integer, primary_key=True)

    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)

    leave_type = Column(String(50), nullable=False)
    total = Column(Integer, nullable=False)
    used = Column(Integer, default=0, nullable=False)
    remaining = Column(Integer, nullable=False)

    employee = relationship("Employee")
