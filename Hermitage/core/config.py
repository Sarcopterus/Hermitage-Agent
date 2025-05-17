# Hermitage/core/config.py

"""
Módulo de configuración central para Hermitage Agency.

Este módulo gestiona la instanciación de modelos de lenguaje (LLM)
y modelos de embeddings, así como la definición de rutas clave
del proyecto para asegurar consistencia y facilitar modificaciones.
"""

import os
from langchain_openai import OpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Para cargar variables como OPENAI_API_KEY

# --- Configuración de Modelos ---
OPENAI_LLM_MODEL_NAME = "gpt-3.5-turbo-instruct"
OPENAI_EMBEDDINGS_MODEL_NAME = "text-embedding-ada-002"

def get_llm_instance():
    """Retorna una instancia configurada del LLM."""
    return OpenAI(model_name=OPENAI_LLM_MODEL_NAME)

def get_embeddings_instance():
    """Retorna una instancia configurada del modelo de embeddings."""
    return OpenAIEmbeddings(model=OPENAI_EMBEDDINGS_MODEL_NAME)

# --- Rutas del Proyecto ---
BASE_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERMITAGE_DIR = os.path.join(BASE_PROJECT_DIR, "Hermitage")
VECTORSTORE_PATH = os.path.join(HERMITAGE_DIR, "vectorstore")
DEMO_DOCS_PATH = os.path.join(HERMITAGE_DIR, "Data", "demo_docs")
