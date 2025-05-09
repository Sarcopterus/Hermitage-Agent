import logging
from datetime import datetime
import os

# Crear carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

# Configuración del logger
logging.basicConfig(
    filename=f"logs/agent_log_{datetime.now().strftime('%Y-%m-%d')}.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] %(message)s",
    encoding="utf-8"
)

def log_interaction(user_input: str, agent_name: str, response: str):
    logging.info(f"Usuario preguntó: {user_input}")
    logging.info(f"Agente: {agent_name}")
    logging.info(f"Respuesta: {response}\n")
    logging.info("-" * 50)  # Separador entre interacciones 