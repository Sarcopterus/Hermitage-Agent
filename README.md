# 🤖 Hermitage AI Agent Suite

Este repositorio contiene una suite de agentes inteligentes diseñados para **Hermitage Agency**, cada uno con funciones especializadas para asistir en tareas empresariales, automatización y generación de contenido.

---

## 📦 Estructura del Proyecto

ChatGPT dijo:
Perfecto. Aquí tienes un README.md inicial completo, listo para copiar y guardar en la raíz del proyecto:

markdown
Copiar
Editar
# 🤖 Hermitage AI Agent Suite

Este repositorio contiene una suite de agentes inteligentes diseñados para **Hermitage Agency**, cada uno con funciones especializadas para asistir en tareas empresariales, automatización y generación de contenido.

---

## 📦 Estructura del Proyecto

Hermitage/
├── Agents/
│ ├── main_agent.py
│ ├── support_agent.py
│ ├── content_generator.py
│ ├── automatizer_agent.py
│ └── data_analyzer.py (en progreso)
├── utils/
│ └── logger.py
├── main.py
├── test_vector_db.py
├── build_vector_db.py
└── requirements.txt


---

## 🧠 Agentes Incluidos

- `agente_soporte`: Responde preguntas internas usando documentación.
- `agente_contenido`: Genera posts, copys y nombres creativos para marketing.
- `agente_automatizador`: Diseñado para automatizar tareas repetitivas.
- `agente_analisis`: Analizará datos (en desarrollo).
- `agente_principal`: El coordinador que delega la tarea al agente correcto.

---

## 🚀 Cómo ejecutar

1. Clona el repositorio:
   git clone https://github.com/Sarcopterus/Hermitage-Agent.git
   cd Hermitage-Agent

2. Crea el entorno virtual y actívalo:
    python -m venv venv
    venv\Scripts\activate  # Windows 
    
3. Instala dependencias:
   pip install -r requirements.txt

4. Agrega tu .env con tu clave OpenAI:

5. Ejecuta el agente principal:
   python -m Hermitage.main

