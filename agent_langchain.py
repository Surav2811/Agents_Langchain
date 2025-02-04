import langchain
from langchain.agents import initialize_agent, load_tools
from langchain.tools import Tool
from langchain.llms import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain_community.tools import DuckDuckGoSearchRun
# Web Search Tool using DuckDuckGo
search_tool = Tool(
    name="DuckDuckGo Search",
    func=DuckDuckGoSearchRun().run,
    description="Useful for real-time web searches."
)

from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

# Initialize the Wikipedia Tool
wikipedia_tool = Tool(
    name="Wikipedia Search",
    func=WikipediaAPIWrapper().run,
    description="Best for quick factual information from Wikipedia."
)

from langchain_community.tools.arxiv.tool import ArxivQueryRun

# Arxiv Search Tool
arxiv_tool = Tool(
    name="Arxiv Search",
    func=ArxivQueryRun().run,
    description="Great for finding academic papers and research articles. Provide topics, authors, or keywords."
)

llm = OpenAI(temperature=0.5)

tools = [search_tool, wikipedia_tool,arxiv_tool]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True, handle_parsing_errors=True)

#Query 1
response = agent.run("What's the temperature in Delhi now?")

print(response)

#Query 2
query = "Search for any 3 research papers on Diffusion Models in 2024."
response = agent.run(query)
print("Response from Agent:")
print(response)

#Query 3
query = "Imdb rating of shawshank redemption ?."
response = agent.run(query)
print("Response from Agent:")
print(response)

#Query 4
query = "Name the latest model of deep-seek?."
response = agent.run(query)
print("Response from Agent:")
print(response)