from agents import Agent, function_tool
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain.chains import RetrievalQA

# Cargar vectorstore y configurar cadena QA
vectorstore = FAISS.load_local(
    "vectorstore",
    OpenAIEmbeddings(),
    allow_dangerous_deserialization=True  # Asegúrate de validar que el contenido es seguro
)
retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    retriever=retriever,
    return_source_documents=True
)

@function_tool
def buscar_en_documentos(pregunta: str) -> str:
    """Responde preguntas frecuentes internas usando los documentos de Hermitage."""
    return qa_chain.run(pregunta)

# Registrar el agente
agente_soporte = Agent(
    name="Agente de Soporte Hermitage",
    instructions="Responde preguntas internas de empleados usando documentación oficial.",
    tools=[buscar_en_documentos]
)
