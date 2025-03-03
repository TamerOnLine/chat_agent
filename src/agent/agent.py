from tools.weather_tool import weather_tool
from tools.stock_tool import stock_tool
from tools.custom_tool import custom_tool
from tools.internet_search_tool import internet_search_tool

from model.ollama_model import OllamaHandler
from langchain.agents import initialize_agent, AgentType


class Agent:
    """AI agent integrating weather, stock, and a fallback tool using LangChain."""

    def __init__(self):
        """Initialize the AI agent with tools."""
        self.handler = OllamaHandler()  
        self.tools = [weather_tool, stock_tool, custom_tool, internet_search_tool]  

       
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.handler.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            allowed_tools=[
                        "Use the Weather API",
                        "StockPrice",
                        "GeneralResponse",
                        "InternetSearch"
                        ],
            handle_parsing_errors=True
        )

    def process(self, query):
        """
        Pass the query to the agent to determine the appropriate tool.

        Args:
            query (str): User query.

        Returns:
            str: The agent's response.
        """
        response = self.agent.invoke(query)
        return response["output"]
