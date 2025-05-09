# 🧠 Hermitage AI Assistant

Asistente inteligente modular para Hermitage Agency.  
Este sistema orquesta múltiples agentes especializados para asistir en:

- 📄 Soporte interno basado en documentación (FAQs, políticas, etc.)
- ✨ Generación creativa de contenido para redes y campañas
- 🔁 Automatización de tareas repetitivas
- 📊 Análisis de datos para campañas y redes sociales *(en desarrollo)*

## 📁 Estructura del proyecto

Hermitage/
│
├── Agents/
│ ├── support_agent.py
│ ├── content_generator.py
│ ├── automatizer_agent.py
│ ├── data_analyzer.py # (por construir)
│ └── main_agent.py
│
├── utils/
│ ├── logger.py
│ └── load_documents.py
│
├── vectorstore/ # Base de conocimiento embebida
├── logs/ # Logs de uso del sistema
├── main.py # Punto de entrada para pruebas
└── .env # Variables sensibles (NO incluir en Git)


## 🚀 Ejecución
python -m Hermitage.main

## Requisitos:
pip install -r requirements.txt

##🛡️ Seguridad:
Configura tu clave OpenAI en el archivo .env: