from dotenv import load_dotenv
load_dotenv()
from Hermitage.agents import Agent, function_tool
from Hermitage.agents.support_agent import agente_soporte

# from Hermitage.analytics_agent import agente_analitico  # ejemplo futuro

# Crear el agente principal
main_agent = Agent(
    name="Hermitage AI Assistant",
    instructions=(
        "Eres el asistente principal de Hermitage. "
        "Puedes delegar tareas a otros agentes según el tipo de pregunta. "
        "Usa el agente de soporte para preguntas internas y el agente creativo para ideas de marketing."
    ),
    tools=[
        agente_soporte,
        agente_creativo  # si existe
    ]
)

# Entrada de prueba
if __name__ == "__main__":
    pregunta = "¿Cuál es la política de vacaciones en Hermitage?"
    respuesta = main_agent.run(pregunta)
    print("🧠 Respuesta del asistente principal:\n", respuesta)
