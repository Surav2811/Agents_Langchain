This is implementation of an AI Agent using OpenAI API key. It searches internet based on user query while using tools like duckduckgo etc and then process the result of the search and then give you a final response.

You can also use Ollama, if you do not want to get charged for the API costs.
Any time that we have code like:
openai = OpenAI()

You can use this as a direct replacement:
openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

Below is a full example:
# You need to do this one time on your computer
!ollama pull llama3.2

from openai import OpenAI
MODEL = "llama3.2"
openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
response = openai.chat.completions.create(
 model=MODEL,
 messages=[{"role": "user", "content": "What is 2 + 2?"}]
)
print(response.choices[0].message.content)



2. Added the Agent functionality to have RAG chat with any website. Populate the website you want the info about.
