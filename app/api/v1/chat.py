from fastapi import APIRouter
from pydantic import BaseModel

from app.api.v1.views import call_agent

router = APIRouter()


class ChatRequest(BaseModel):
    employee_id: int
    message: str


@router.post("/chat")
async def chat(req: ChatRequest):
    response = await call_agent(req.employee_id, req.message)
    return {"reply": response}
