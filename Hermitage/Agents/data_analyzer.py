from Hermitage.agents import Agent, function_tool
from Hermitage.core.config import get_llm_instance
from dotenv import load_dotenv
load_dotenv()


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

@function_tool
def analizar_macrotendencias(sector: str, region: str) -> str:
    """Identifica macrotendencias globales que impactan un sector en una región determinada."""
    prompt = f"¿Cuáles son las macrotendencias globales que afectan al sector '{sector}' en la región de '{region}'? Incluye impacto tecnológico, social, económico y ambiental."
    return llm.invoke(prompt)

@function_tool
def construir_matriz_anfoda(marca: str, contexto: str) -> str:
    """Construye una matriz AMOFODA considerando factores internos y externos."""
    prompt = f"Construye una matriz AMOFODA (Aspiraciones, Motivadores, Oportunidades, Fortalezas, Debilidades, Amenazas) para la marca '{marca}' en el contexto: {contexto}."
    return llm.invoke(prompt)

@function_tool
def simular_decision_estrategica(caso: str, opciones: str) -> str:
    """Simula una decisión ejecutiva comparando distintas estrategias posibles."""
    prompt = f"Simula una decisión estratégica para el siguiente caso: {caso}. Compara estas opciones: {opciones}. Evalúa riesgos, beneficios y escenario óptimo."
    return llm.invoke(prompt)

@function_tool
def planificar_ingreso_nuevo_mercado(pais: str, industria: str) -> str:
    """Diseña una estrategia de entrada para un nuevo mercado."""
    prompt = f"Diseña un plan de entrada al mercado en '{pais}' para una empresa del sector '{industria}'. Incluye barreras, posicionamiento y canales recomendados."
    return llm.invoke(prompt)

@function_tool
def mapear_ecosistema_startups(sector: str, ubicacion: str) -> str:
    """Identifica actores clave, innovaciones y alianzas potenciales en el ecosistema de startups."""
    prompt = f"Mapea el ecosistema de startups en '{ubicacion}' para el sector '{sector}'. Incluye actores disruptivos, oportunidades de alianza e inspiración para innovación."
    return llm.invoke(prompt)

# Registrar el agente
agente_estratega = Agent(
    name="Agente Estratégico Hermitage",
    instructions="Define visión, estrategia y posicionamiento competitivo. Usa tus herramientas para diseñar planes sostenibles.",
    tools=[
        analizar_competencia,
        proponer_estrategia_crecimiento,
        crear_mision_vision,
        evaluar_modelo_negocio,
        diseñar_ventaja_competitiva,
        definir_propuesta_valor,
        analizar_macrotendencias,
        construir_matriz_anfoda,
        simular_decision_estrategica,
        planificar_ingreso_nuevo_mercado,
        mapear_ecosistema_startups
    ]
)
