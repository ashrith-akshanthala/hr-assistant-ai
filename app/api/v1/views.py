from app.llm.v1.runtime.chat import chat as chat_v1


async def call_agent(employee_id: int, message: str):
    print("in call agent")
    result = chat_v1({"employee_id": employee_id, "message": message})
    return result
