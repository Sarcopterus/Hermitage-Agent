from agents import Agent, function_tool
from langchain_community.llms import OpenAI

llm = OpenAI()

@function_tool
def generar_post_instagram(marca: str, producto: str) -> str:
    """Genera una publicación creativa de Instagram para un producto."""
    prompt = f"Redacta un post atractivo de Instagram para {marca}, promocionando su producto {producto}. Usa un tono informal y creativo."
    return llm.invoke(prompt)

@function_tool
def sugerir_nombre_campaña(objetivo: str, público_objetivo: str) -> str:
    """Sugiere un nombre creativo para una campaña de marketing."""
    prompt = f"Sugiere un nombre llamativo para una campaña cuyo objetivo es '{objetivo}' y está dirigida a '{público_objetivo}'."
    return llm.invoke(prompt)

@function_tool
def redactar_copy_promocional(producto: str, tono: str = "emocional") -> str:
    """Redacta un copy promocional breve para un producto en el tono indicado."""
    prompt = f"Escribe un copy de marketing para el producto '{producto}' en un tono {tono}."
    return llm.invoke(prompt)

# Registrar el agente
agente_contenido = Agent(
    name="Agente Creativo Hermitage",
    instructions="Eres experto en contenido publicitario y marketing. Usa tus herramientas para generar ideas creativas.",
    tools=[
        generar_post_instagram,
        sugerir_nombre_campaña,
        redactar_copy_promocional
    ]
)
