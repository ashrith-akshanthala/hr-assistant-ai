from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.postgres import SessionLocal
from app.models import Employee


class EmployeeService:

    @staticmethod
    def get_employee(employee_id: int):
        db: Session = SessionLocal()

        try:
            stmt = select(Employee).where(Employee.id == employee_id)
            employee = db.execute(stmt).scalar_one_or_none()

            if not employee:
                return {"error": "Employee not found"}

            return {
                "id": employee.id,
                "name": employee.name,
                "email": employee.email,
                "department": employee.department,
                "role": employee.role,
                "is_active": employee.is_active,
            }

        except Exception as e:
            return {"error": str(e)}

        finally:
            db.close()
