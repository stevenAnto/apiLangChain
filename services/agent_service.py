from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from config import Config


class AgentService:
    def __init__(self):
        # Herramientas
        wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1))
        tavily_tool = TavilySearchResults(tavily_api_key=Config.TAVILY_API_KEY)
        tools = [wikipedia_tool, tavily_tool]

        # Modelo
        llm = ChatOpenAI(model=Config.MODEL_NAME, api_key=Config.OPENAI_API_KEY)

        # Prompt de la comunidad
        prompt = hub.pull("hwchase17/openai-functions-agent")

        # Crear agente
        agent = create_tool_calling_agent(llm, tools, prompt=prompt)

        # Ejecutar
        self.agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    def get_response(self, user_input: str) -> str:
        try:
            result = self.agent_executor.invoke({"input": user_input})
            return result["output"]
        except Exception as e:
            return f"Error: {str(e)}"

# Instancia singleton
agent_service = AgentService()