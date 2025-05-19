from dotenv import load_dotenv
load_dotenv()
from Hermitage.agents import Agent, function_tool
from Hermitage.core.config import get_llm_instance
llm = get_llm_instance()


llm = OpenAI()

@function_tool
def generar_script_email(asunto: str, cuerpo_base: str) -> str:
    """Genera un script de Python para enviar correos automatizados."""
    prompt = f"Crea un script de Python que envíe un email con asunto '{asunto}' y este cuerpo base: {cuerpo_base}. Usa smtplib y email.message."
    return llm.invoke(prompt)

@function_tool
def generar_script_python(descripcion_tarea: str) -> str:
    """Genera un script de Python para automatizar una tarea técnica simple."""
    prompt = f"Genera un script de Python para automatizar la siguiente tarea: {descripcion_tarea}."
    return llm.invoke(prompt)

@function_tool
def proponer_flujo_automatizacion(departamento: str) -> str:
    """Sugiere un flujo de tareas automatizables en un departamento específico."""
    prompt = f"Sugiere un flujo de tareas que podrían automatizarse en el departamento de {departamento}."
    return llm.invoke(prompt)

@function_tool
def generar_plantilla_correo_escenario(escenario: str) -> str:
    """Genera una plantilla de correo para un escenario típico de comunicación interna o externa."""
    prompt = f"Crea una plantilla de correo efectiva para este escenario: {escenario}."
    return llm.invoke(prompt)

@function_tool
def sugerir_integracion_herramientas(herramientas: str) -> str:
    """Sugiere una integración automatizada entre las herramientas mencionadas."""
    prompt = f"Sugiere una forma de automatizar flujos entre las siguientes herramientas: {herramientas}. Incluye ejemplos o herramientas como Zapier o Make."
    return llm.invoke(prompt)

@function_tool
def crear_politica_automatizacion(departamento: str) -> str:
    """Genera una política interna para la implementación de automatización en un departamento."""
    prompt = f"Redacta una política interna para automatizar tareas en el departamento de {departamento}."
    return llm.invoke(prompt)

@function_tool
def detectar_redundancias_descripcion(descripcion: str) -> str:
    """Detecta redundancias o ineficiencias en una descripción de procesos."""
    prompt = f"Analiza esta descripción de procesos y detecta redundancias o tareas ineficientes: {descripcion}"
    return llm.invoke(prompt)

@function_tool
def generar_script_sistema(descripcion: str, sistema: str = "Windows") -> str:
    """Genera un script para automatización según sistema operativo."""
    prompt = f"Genera un script para {sistema} que automatice la siguiente tarea: {descripcion}."
    return llm.invoke(prompt)

# Registrar el agente
agente_automatizador = Agent(
    name="Agente Automatizador Hermitage",
    instructions="Proporciona soluciones técnicas o conceptuales de automatización para procesos internos.",
    tools=[
        generar_script_email,
        generar_script_python,
        proponer_flujo_automatizacion,
        generar_plantilla_correo_escenario,
        sugerir_integracion_herramientas,
        crear_politica_automatizacion,
        detectar_redundancias_descripcion,
        generar_script_sistema
    ]
)
