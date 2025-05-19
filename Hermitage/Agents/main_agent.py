from Hermitage.agents import Agent
from Hermitage.agents.support_agent import agente_soporte
from Hermitage.agents.content_generator import agente_contenido
from Hermitage.agents.automatizer_agent import agente_automatizador
from Hermitage.agents.data_analyzer import agente_analisis
from Hermitage.agents.strategy_agent import agente_estratega 
from dotenv import load_dotenv
load_dotenv()


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
        agente_analisis,
        agente_estratega
    ]
)
