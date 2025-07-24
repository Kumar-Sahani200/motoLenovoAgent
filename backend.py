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
    return  """
    <h2>Welcome to the MotoLeno Agent API!</h2>
    <p>This API provides information about Motorola and Lenovo devices.</p>
    <p>
        <a href="https://motolenovoagent.onrender.com/docs" target="_blank">API Endpoint</a><br>
        <a href="https://github.com/Kumar-Sahani200/motoLenovoAgent" target="_blank">Git Repository</a><br>
        <a href="https://miro.com/app/board/uXjVJbEjR4U=/?share_link_id=258247562034" target="_blank">System Design</a>
    </p>
    """

@app.post("/chat")
def chat(request: RequestState):
    """API endpoint to handle chat requests"""

    res=getAgentRes(request.query)

    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)


