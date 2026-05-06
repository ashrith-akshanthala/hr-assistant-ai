from langchain.tools import ToolRuntime, tool

from app.services.employee_service import EmployeeService


@tool
def get_employee(runtime: ToolRuntime) -> dict:
    """Get Current Employee data."""

    context = runtime.context
    print(context)

    if context is None:
        return {"error": "Missing context"}

    employee_id = context.employee_id
    return EmployeeService.get_employee(employee_id)
