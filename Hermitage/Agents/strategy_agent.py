from Hermitage.agents import Agent, function_tool
from Hermitage.agents.shared_tools.strategic_analysis_tools import (
    analizar_competencia,
    proponer_estrategia_crecimiento,
    crear_mision_vision,
    evaluar_modelo_negocio,
    diseñar_ventaja_competitiva,
    definir_propuesta_valor
)

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
        definir_propuesta_valor
    ]
)
