from pydantic import BaseModel, Field
from fastapi import FastAPI
from agent import getAgentRes
import uvicorn

class RequestState(BaseModel):
    query: str = Field(..., example="What is the latest Motorola phone?")


app = FastAPI()


@app.get("/")
def read_root():   
    """Root endpoint to check if the server is running"""
    return {"message": "Welcome to the MotoLeno Agent API!",
            "description": "This API provides information about Motorola and Lenovo devices.",
            "api endpoint": "https://motolenovoagent.onrender.com/docs", 
            "git repository": "https://github.com/Kumar-Sahani200/motoLenovoAgent",
            "System Design": "https://miro.com/app/board/uXjVJbEjR4U=/?share_link_id=258247562034"}

@app.post("/chat")
def chat(request: RequestState):
    """API endpoint to handle chat requests"""

    res=getAgentRes(request.query)

    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)


