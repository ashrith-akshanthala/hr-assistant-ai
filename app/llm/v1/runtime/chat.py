from app.llm.v1.context.request import RequestContext
from app.llm.v1.core.agent import invoke_agent


def chat(data: dict):
    message = data["message"]
    employee_id = data["employee_id"]

    context = RequestContext(employee_id=employee_id)

    print("invoking agent")

    return invoke_agent(message, context)
