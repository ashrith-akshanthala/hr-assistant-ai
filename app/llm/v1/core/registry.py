from app.llm.v1.tools.employee import get_employee
from app.llm.v1.tools.leave import get_employee_leaves


def get_tools():
    return [get_employee, get_employee_leaves]
