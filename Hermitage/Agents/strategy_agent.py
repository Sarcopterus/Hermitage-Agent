from agents import Agent, function_tool
from langchain_community.llms import OpenAI

llm = OpenAI()

@function_tool
def analizar_competencia(marca: str, sector: str) -> str:
    """Realiza un análisis estratégico de competencia para una marca en un sector específico."""
    prompt = f"Analiza estratégicamente la posición de la marca {marca} dentro del sector {sector}. Incluye fortalezas, debilidades y oportunidades competitivas."
    return llm.invoke(prompt)

@function_tool
def proponer_estrategia_crecimiento(pais: str, tipo_negocio: str) -> str:
    """Sugiere una estrategia de crecimiento para un tipo de negocio en un país determinado."""
    prompt = f"Propón una estrategia de crecimiento sostenible para un {tipo_negocio} que opera en {pais}. Considera tendencias del mercado, comportamiento del consumidor y factores locales."
    return llm.invoke(prompt)

@function_tool
def crear_mision_vision(valores: str, publico: str) -> str:
    """Genera una misión y visión empresarial basadas en valores y público objetivo."""
    prompt = f"Redacta una misión y visión claras y diferenciadoras para una empresa con estos valores: {valores}, dirigida a {publico}."
    return llm.invoke(prompt)

# Registrar el agente
agente_estratega = Agent(
    name="Agente Estratégico Hermitage",
    instructions="Diseña estrategias, analiza competencia y propone planes de crecimiento empresarial.",
    tools=[
        analizar_competencia,
        proponer_estrategia_crecimiento,
        crear_mision_vision
    ]
)
