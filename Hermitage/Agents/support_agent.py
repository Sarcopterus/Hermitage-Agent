from agents import Agent, function_tool
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_core.runnables import RunnableLambda
from langchain_core.documents import Document
from Hermitage.core.config import get_llm_instance, get_embeddings_instance, VECTORSTORE_PATH
import os

# Instancias centralizadas
llm = get_llm_instance()
embeddings = get_embeddings_instance()

# Cargar vectorstore y configurar retriever mejorado
vectorstore = FAISS.load_local(VECTORSTORE_PATH, embeddings, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 4})

# QA Chain con fuentes
qa_chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    retriever=retriever
)

@function_tool
def buscar_en_documentos(pregunta: str) -> str:
    """Responde preguntas internas de empleados usando los documentos oficiales."""
    try:
        result = qa_chain.invoke({"question": pregunta})
        return f"Respuesta: {result['answer']}\n\nFuentes: {result['sources']}"
    except Exception as e:
        return f"[Error procesando la consulta: {str(e)}]"

@function_tool
def resumir_politica(nombre: str) -> str:
    """Resume una política institucional por nombre o tema."""
    query = f"Resume la política institucional sobre {nombre}"
    return buscar_en_documentos(query)

@function_tool
def verificar_actualizacion(politica: str) -> str:
    """Verifica si la política mencionada ha tenido actualizaciones recientes."""
    query = f"¿La política de {politica} ha sido actualizada recientemente?"
    return buscar_en_documentos(query)

@function_tool
def listar_politicas_disponibles() -> str:
    """Lista los documentos disponibles para consulta institucional."""
    try:
        archivos = os.listdir(os.path.join(VECTORSTORE_PATH, "..", "Data", "demo_docs"))
        politicas = [f for f in archivos if f.endswith(".txt")]
        return "\n".join(politicas)
    except Exception as e:
        return f"[Error al listar documentos: {str(e)}]"

@function_tool
def obtener_documento_tema(tema: str) -> str:
    """Devuelve el documento completo sobre un tema específico si está disponible."""
    ruta_base = os.path.join(VECTORSTORE_PATH, "..", "Data", "demo_docs")
    try:
        for f in os.listdir(ruta_base):
            if tema.lower() in f.lower():
                with open(os.path.join(ruta_base, f), "r", encoding="utf-8") as file:
                    return file.read()[:4000] + "... [truncado]"
        return "No se encontró un documento que coincida con ese tema."
    except Exception as e:
        return f"[Error al recuperar documento: {str(e)}]"

@function_tool
def comparar_politicas(politica_1: str, politica_2: str) -> str:
    """Compara dos políticas institucionales y muestra diferencias clave."""
    query = f"Compara las políticas '{politica_1}' y '{politica_2}' en términos de contenido, propósito y aplicación."
    return buscar_en_documentos(query)

@function_tool
def sugerir_preguntas_frecuentes() -> str:
    """Sugiere posibles preguntas frecuentes a partir de los documentos institucionales."""
    query = "Sugiere 5 preguntas frecuentes basadas en las políticas internas de Hermitage."
    return buscar_en_documentos(query)

@function_tool
def detectar_incongruencias_politicas() -> str:
    """Detecta posibles contradicciones entre políticas institucionales existentes."""
    query = "¿Existen contradicciones o inconsistencias en las políticas internas de Hermitage?"
    return buscar_en_documentos(query)

# Registrar el agente
agente_soporte = Agent(
    name="Agente de Soporte Hermitage",
    instructions="Responde preguntas internas de empleados usando documentación oficial institucional.",
    tools=[
        buscar_en_documentos,
        resumir_politica,
        verificar_actualizacion,
        listar_politicas_disponibles,
        obtener_documento_tema,
        comparar_politicas,
        sugerir_preguntas_frecuentes,
        detectar_incongruencias_politicas
    ]
)
