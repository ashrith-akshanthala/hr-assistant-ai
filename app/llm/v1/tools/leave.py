from langchain.tools import ToolRuntime, tool
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.postgres import SessionLocal
from app.models import Leave


@tool
def get_employee_leaves(runtime: ToolRuntime) -> dict:
    """
    Get Current Employee leaves.
    """
    context = runtime.context
    print(context)

    if context is None:
        return {"error": "Missing context"}

    employee_id = context.employee_id

    db: Session = SessionLocal()

    try:
        stmt = select(Leave).filter(Leave.employee_id == employee_id)
        leaves = db.execute(stmt).scalars().all()
        print(leaves)

        if not leaves:
            return {"error": "Employee not found"}

        return leaves

    except Exception as e:
        return {"error": str(e)}

    finally:
        db.close()
