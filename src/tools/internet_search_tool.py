import os
from langchain.tools import Tool
from serpapi import GoogleSearch
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve SerpAPI API key from environment variables
API_KEY = os.getenv("SERPAPI_API_KEY")


def search_internet(query: str) -> str:
    """Search the internet using SerpAPI and return the top results."""
    if not API_KEY:
        return "API_KEY for SerpAPI is missing. Please check your .env file."

    # Improve search query if it's a single keyword
    if len(query.split()) == 1:
        query = f"related:{query}"  # Search for related terms

    params = {
        "q": query,
        "api_key": API_KEY,
        "num": 5,  # Fetch more results
        "hl": "en",  # Ensure results are in English
    }

    search = GoogleSearch(params)
    results = search.get_dict().get("organic_results", [])

    if not results:
        return "No relevant results found."

    return "\n".join([f"{r['title']}: {r['link']}" for r in results]) + "\n"


# Define the internet search tool
internet_search_tool = Tool(
    name="InternetSearch",
    func=search_internet,
    description="Fetches top search results from the internet using SerpAPI.",
    return_direct=True,
)
