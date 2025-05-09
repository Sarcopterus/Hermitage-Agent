import os
import re
import csv
from collections import Counter
from datetime import datetime

def analizar_logs(fecha=None):
    if not fecha:
        fecha = datetime.now().strftime('%Y-%m-%d')
    
    log_path = f"logs/agent_log_{fecha}.log"
    if not os.path.exists(log_path):
        print(f"No hay logs para {fecha}.")
        return

    with open(log_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    preguntas = []
    agentes = []
    respuestas = []

    for line in lines:
        if "Usuario preguntó:" in line:
            preguntas.append(line.strip().split("Usuario preguntó:")[1].strip())
        elif "Agente:" in line:
            agentes.append(line.strip().split("Agente:")[1].strip())
        elif "Respuesta:" in line:
            respuestas.append(line.strip().split("Respuesta:")[1].strip())

    print(f"\n📊 Resumen de actividad - {fecha}")
    print(f"🗂 Total de interacciones: {len(preguntas)}")
    print(f"🧠 Agentes utilizados:")
    for agente, count in Counter(agentes).most_common():
        print(f"   - {agente}: {count} vez/veces")

    print(f"\n🔁 Preguntas frecuentes:")
    for pregunta, count in Counter(preguntas).most_common(5):
        print(f"   - {pregunta} ({count})")

    return {
        "fecha": fecha,
        "total": len(preguntas),
        "agentes": Counter(agentes),
        "preguntas": Counter(preguntas),
        "respuestas": respuestas
    }

def exportar_a_csv(resumen, ruta="logs/summary_export.csv"):
    if not resumen:
        print("❌ No hay datos para exportar.")
        return

    with open(ruta, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Encabezados
        writer.writerow(["Fecha", "Pregunta", "Agente", "Respuesta"])

        for pregunta, agente, respuesta in zip(
            resumen["preguntas"].elements(),
            resumen["agentes"].elements(),
            resumen["respuestas"]
        ):
            writer.writerow([resumen["fecha"], pregunta, agente, respuesta])

    print(f"✅ Exportación exitosa a: {ruta}")

