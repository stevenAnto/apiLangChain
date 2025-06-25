from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config import Config

class ChatService:
    def __init__(self):
        # Inicializar el modelo LLM
        self.llm = ChatOpenAI(
            model=Config.MODEL_NAME,
            api_key=Config.OPENAI_API_KEY
        )
        
        # Crear el prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Eres un asistente de IA, puedes responder a preguntas sobre IA"),
            ("user", "{input}")
        ])
        
        # Crear la cadena
        self.chain = self.prompt | self.llm
    
    def get_response(self, input_text: str) -> str:
        """Obtiene una respuesta del modelo de chat"""
        try:
            response = self.chain.invoke({"input": input_text})
            return response.content
        except Exception as e:
            return f"Error al obtener respuesta: {str(e)}"

# Instancia singleton del servicio
chat_service = ChatService()