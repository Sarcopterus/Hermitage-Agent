from agents import Agent
from Hermitage.Agents.support_agent import agente_soporte
from Hermitage.Agents.content_generator import agente_contenido
from Hermitage.Agents.automatizer_agent import agente_automatizador
from Hermitage.Agents.data_analyzer import agente_analisis

# Crear el agente principal
agente_principal = Agent(
    name="Coordinador General Hermitage",
    instructions="""
    Eres un agente coordinador para Hermitage Agency.
    Tu trabajo es analizar la solicitud del usuario y decidir cuál de los agentes especializados puede manejar mejor la tarea.
    No intentes resolver tú mismo nada. Solo decide a quién delegar.
    """,
    handoffs=[
        agente_soporte,
        agente_contenido,
        agente_automatizador,
        agente_analisis
    ]
)
