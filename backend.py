from pydantic import BaseModel, Field
from fastapi import FastAPI
from agent import getAgentRes
import uvicorn

class RequestState(BaseModel):
    query: str = Field(..., example="What is the latest Motorola phone?")


app = FastAPI()

@app.post("/chat")
def chat(request: RequestState):
    """API endpoint to handle chat requests"""

    res=getAgentRes(request.query)

    return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)


