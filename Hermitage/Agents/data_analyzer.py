from agents import Agent, function_tool
from langchain_community.llms import OpenAI
from typing import List
import pandas as pd

llm = OpenAI()

@function_tool
def resumir_csv_con_insights(ruta_archivo: str) -> str:
    """
    Analiza un archivo CSV y devuelve un resumen con insights clave.
    Ejemplo de insights: valores atípicos, correlaciones, tendencias generales.
    """
    try:
        df = pd.read_csv(ruta_archivo)
        resumen = df.describe().to_string()
        prompt = f"Aquí hay un resumen estadístico de un dataset:\n{resumen}\nGenera insights clave, patrones o posibles anomalías."
        return llm.invoke(prompt)
    except Exception as e:
        return f"[Error al analizar CSV: {str(e)}]"

@function_tool
def generar_recomendaciones_comerciales(descripcion_datos: str) -> str:
    """
    A partir de una descripción de datos, genera ideas o estrategias comerciales.
    """
    prompt = f"A partir de estos datos: {descripcion_datos}, sugiere recomendaciones para marketing o estrategia empresarial."
    return llm.invoke(prompt)

# Registrar el agente
agente_analisis = Agent(
    name="Agente de Análisis de Datos Hermitage",
    instructions="Realiza análisis e interpretación de datos para informar decisiones estratégicas.",
    tools=[
        resumir_csv_con_insights,
        generar_recomendaciones_comerciales
    ]
)
