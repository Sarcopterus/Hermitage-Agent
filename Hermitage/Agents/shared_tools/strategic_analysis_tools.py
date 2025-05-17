"""
Herramientas compartidas para análisis estratégico.
Estas funciones son utilizadas tanto por el agente de estrategia como por el de análisis de datos.
"""

from agents import function_tool
from Hermitage.core.config import get_llm_instance

llm = get_llm_instance()

@function_tool
def analizar_competencia(marca: str, sector: str) -> str:
    """Análisis estratégico de la competencia de una marca en un sector específico."""
    prompt = f"Realiza un análisis competitivo de la marca {marca} en el sector {sector}. Incluye fortalezas, debilidades, amenazas y oportunidades (FODA)."
    return llm.invoke(prompt)

@function_tool
def proponer_estrategia_crecimiento(pais: str, tipo_negocio: str) -> str:
    """Sugerencia de estrategia de crecimiento empresarial adaptada a un país y tipo de negocio."""
    prompt = f"Propón una estrategia de crecimiento sostenible para un {tipo_negocio} en {pais}. Incluye canales de expansión, innovación y diferenciación."
    return llm.invoke(prompt)

@function_tool
def crear_mision_vision(valores: str, publico: str) -> str:
    """Generación de misión y visión alineadas con valores y público objetivo."""
    prompt = f"Redacta misión y visión para una empresa con estos valores: {valores}, orientada a {publico}. Sé inspirador pero claro."
    return llm.invoke(prompt)

@function_tool
def evaluar_modelo_negocio(descripcion: str) -> str:
    """Evaluación de la viabilidad y sostenibilidad de un modelo de negocio propuesto."""
    prompt = f"Evalúa el siguiente modelo de negocio: {descripcion}. ¿Es viable, sostenible y competitivo? ¿Qué mejorarías?"
    return llm.invoke(prompt)

@function_tool
def diseñar_ventaja_competitiva(mercado: str, oferta: str) -> str:
    """Diseña una ventaja competitiva sólida para un producto o servicio."""
    prompt = f"En el mercado {mercado}, diseña una ventaja competitiva clara y defendible para esta oferta: {oferta}."
    return llm.invoke(prompt)

@function_tool
def definir_propuesta_valor(cliente: str, necesidad: str) -> str:
    """Define una propuesta de valor única y diferenciadora para un cliente objetivo."""
    prompt = f"Para un cliente tipo '{cliente}' con esta necesidad: '{necesidad}', define una propuesta de valor convincente."
    return llm.invoke(prompt)
