import os

GROQ_API_KEY = os.environ.get("groqKey")
TAVILY_API_KEY = os.environ.get("travilyKey")

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage


groqLLM=ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

SysPrompt = (
    "You are a helpful, intelligent assistant that only answers queries related to Motorola or Lenovo devices. "
    "Before answering, search the web to ensure your response reflects the most accurate and up-to-date product information. "
    "Motorola and Lenovo offer a wide variety of products beyond just smartphones and laptops, including earbuds, tablets, wearables, accessories, and more — this varies by region and product cycle. "
    "Do not assume either brand's product range is limited unless confirmed by your search. "
    "If someone asks about Lenovo phones, clarify they’re branded under Motorola. "
    "If the query is not about Motorola or Lenovo, politely respond that you only handle Motorola or Lenovo products, and vary your tone naturally. "
    "Keep responses under 100 words and helpful in tone."
)


tools=[TavilySearchResults(max_results=10, tavily_api_key=TAVILY_API_KEY)]


def getAgentRes(query):

    agent=create_react_agent(
            model=groqLLM,
            tools=tools,
            prompt=SysPrompt,
    )

    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    aiMess=[message.content for message in messages if isinstance(message, AIMessage)]
    return aiMess[-1]
