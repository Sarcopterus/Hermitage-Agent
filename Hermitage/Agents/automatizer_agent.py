from agents import Agent, function_tool
from langchain_community.llms import OpenAI

llm = OpenAI()

@function_tool
def generar_script_email(asunto: str, cuerpo_base: str) -> str:
    """Genera un script automatizado para enviar correos internos o masivos."""
    prompt = f"Redacta un script de email formal con asunto '{asunto}' y el siguiente cuerpo base: '{cuerpo_base}'"
    return llm.invoke(prompt)

@function_tool
def generar_script_python(descripcion_tarea: str) -> str:
    """Genera un script en Python para automatizar una tarea técnica simple."""
    prompt = f"Genera un script en Python que automatice la siguiente tarea: {descripcion_tarea}"
    return llm.invoke(prompt)

@function_tool
def proponer_flujo_automatizacion(departamento: str) -> str:
    """Sugiere un flujo de tareas que podrían automatizarse en un departamento específico."""
    prompt = f"Sugiere tareas repetitivas o susceptibles de automatización en el departamento de {departamento}."
    return llm.invoke(prompt)

agente_automatizador = Agent(
    name="Agente Automatizador Hermitage",
    instructions="Propone soluciones de automatización o genera scripts para tareas internas.",
    tools=[
        generar_script_email,
        generar_script_python,
        proponer_flujo_automatizacion
    ]
)
