# 🧠 Hermitage AI Agent System

Sistema modular de agentes de inteligencia artificial diseñado para asistir al equipo de Hermitage Agency en tareas de contenido, soporte y automatización.

---

## 🗂 Estructura del proyecto

ai_marketing_agent/
├── Hermitage/
│ ├── Agents/ # Lógica de agentes específicos
│ ├── Tools/ # Herramientas utilizadas por los agentes
│ ├── utils/ # Análisis, carga de documentos y logs
│ ├── logs/ # Registros de interacciones por fecha
│ ├── vectorstore/ # Embeddings generados con FAISS
│ ├── main.py # Entrada principal para ejecutar agentes
│ ├── dashboard.py # Dashboard con Streamlit
│ └── analyze_logs.py # Analizador y exportador de logs
├── .env # Variables de entorno (no compartir)
├── requirements.txt # Dependencias del proyecto
├── start_hermitage.bat # Lanzador con menú interactivo
└── venv/ # Entorno virtual local


---

## 🚀 Funcionalidades

- **Agentes inteligentes**: delegación dinámica según tipo de solicitud.
- **Soporte basado en documentos internos**: RAG con embeddings de FAISS.
- **Generación y análisis de contenido**.
- **Dashboard interactivo con métricas por agente**.
- **Análisis y exportación de logs diarios a CSV**.
- **Menú por terminal para facilitar pruebas y flujo de trabajo**.

---

## 🧪 ¿Cómo iniciar?

1. Clona el repositorio:
   ```bash
   git clone <repo-url>
   cd ai_marketing_agent

2. Crea y activa entorno virtual:
    python -m venv venv
    .\venv\Scripts\activate

3. Instala las dependencias:
    pip install -r requirements.txt

4.Ejecuta el menú interactivo:
   start_hermitage.bat

⚙️ Requisitos
Python 3.10+

API Key de OpenAI válida (.env)

Windows (recomendado por el uso del .bat)

