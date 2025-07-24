import os

GROQ_API_KEY = os.environ.get("groqKey")
TAVILY_API_KEY = os.environ.get("travilyKey")

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage


groqLLM=ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

SysPrompt="Act as a helpful assistant You can answer questions, provide information, and assist with various queries related to motorola or Lenovo devices. If you don't know the answer, you can search the web for information. limit your responses to 100 words. Only response to questions related to Motorola or lenovo devices, if the question is not related to Motorola or Lenovo devices, then respond with 'I can only answer questions related to Motorola or Lenovo devices.'"
query="What is the latest motorola phone?"

tools=[TavilySearchResults(max_results=5, tavily_api_key=TAVILY_API_KEY)]

agent=create_react_agent(
        model=groqLLM,
        tools=tools,
        prompt=SysPrompt,
)

state={"messages": query}
response=agent.invoke(state)
messages=response.get("messages")
ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
refinedResponse=ai_messages[-1]

print(refinedResponse)