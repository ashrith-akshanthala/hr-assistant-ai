from fastapi import FastAPI

from app.api.v1.chat import router as chat_router_v1

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(chat_router_v1)
