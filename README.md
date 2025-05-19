🤖 Hermitage Agent Suite
Bienvenido a Hermitage Agent Suite: una plataforma modular de agentes inteligentes para potenciar, automatizar y escalar los procesos de Hermitage Agency.
Desarrollada en Python, integra IA avanzada, automatización, análisis de datos y un sistema robusto de reservas de espacios.

📦 Estructura del Proyecto
Hermitage-Agent/
├── Hermitage/
│   ├── agents/
│   │   ├── main_agent.py
│   │   ├── support_agent.py
│   │   ├── content_generator.py
│   │   ├── automatizer_agent.py
│   │   ├── data_analyzer.py
│   │   ├── strategy_agent.py
│   │   ├── chatbot_agenda.py
│   ├── core/
│   │   └── config.py
│   ├── utils/
│   │   ├── agenda_db.py
│   │   ├── herramientas_agenda.py
│   │   ├── servicios_catalogo.py
│   │   ├── logger.py
│   ├── api/
│   │   └── agenda_api.py
│   ├── main.py
│   ├── dashboard.py
├── requirements.txt
├── README.md


🧠 Agentes Disponibles
Agente Principal: Orquesta y delega tareas a los agentes según la consulta.

Agente de Soporte: Responde dudas institucionales usando la documentación interna (vectorstore/FAISS + LLM).

Generador de Contenido: Produce copys, posts y campañas creativas.

Agente Automatizador: Ejecuta tareas repetitivas y flujos automáticos.

Data Analyzer: Análisis de datos empresariales (en desarrollo).

Estratega: Estrategias de negocio y análisis competitivo.

Chatbot de Agenda: Agenda espacios de la agencia (Podcast, Live Stream, Fotografía) vía CLI o API.

🚀 Instalación y Primeros Pasos
1. Clonar el repositorio
bash
Copiar
Editar
git clone https://github.com/Sarcopterus/Hermitage-Agent.git
cd Hermitage-Agent
2. Configurar entorno Python
Instala pyenv y crea un entorno virtual con Python 3.11.9:

bash
Copiar
Editar
pyenv install 3.11.9
pyenv virtualenv 3.11.9 hermitage-env
pyenv activate hermitage-env
3. Instalar dependencias
bash
Copiar
Editar
pip install -r requirements.txt
4. Configurar variables de entorno
Copia el archivo de ejemplo y añade tu API Key real de OpenAI:

bash
Copiar
Editar
cp Hermitage/core/.env.example Hermitage/core/.env
¡No subas nunca tu .env!
(Verifica que .gitignore lo proteja).

💻 Uso del Chatbot de Agenda (CLI)
Desde consola, ejecuta:

bash
Copiar
Editar
python -m Hermitage.agents.chatbot_agenda
Sigue las instrucciones para agendar espacios (servicios activos: Podcast, Live Stream, Fotografía).
También puedes acceder a funciones administrativas (listar, cancelar reservas) escribiendo admin o reservas en el chat.

🖥️ API REST de Agenda (FastAPI)
Permite integrar la agenda con aplicaciones web, móviles, bots o dashboards.

Correr el API
bash
Copiar
Editar
uvicorn Hermitage.api.agenda_api:app --reload
Visita http://127.0.0.1:8000/docs para probar los endpoints en Swagger UI.

Endpoints Disponibles
POST /reservar/ — Crear nueva reserva

GET /reservas/ — Listar reservas actuales

DELETE /reservar/{reserva_id}/ — Cancelar reserva por ID

🛡️ Seguridad y Buenas Prácticas
Variables de entorno y claves: Nunca subas tu .env ni claves privadas.

Historial limpio: Si alguna vez expusiste una clave, sigue el procedimiento BFG y rota la clave.

Dependencias seguras: Usa siempre el entorno virtual y revisa con pip-audit regularmente.

Manejo de errores: El sistema valida fechas, horarios y servicios. Los errores críticos son informados y logueados.

Autenticación: Si expones el API a internet, añade autenticación básica o JWT según necesidad.

🛠️ Comandos Administrativos (CLI)
Listar reservas:
Accede al menú admin (admin o reservas) y elige “Listar reservas”.

Cancelar reservas:
Desde el mismo menú, elige “Cancelar reserva” e ingresa el ID.

✍️ Aportar al proyecto
Haz un fork del repositorio.

Trabaja siempre en una rama.

Haz pull requests bien documentados.

Sigue la convención de código y comentarios.

Respeta las buenas prácticas de seguridad.

👨‍💻 Stack & Tecnologías
Python 3.11.9 (pyenv, virtualenv)

FastAPI

LangChain

OpenAI API (GPT-4o y embeddings)

Streamlit (próximamente para dashboard)

SQLite / SQLAlchemy

dotenv, rich, FAISS, etc.

📚 Ejemplos de uso
CLI
less
Copiar
Editar
Tú: Quiero reservar el set de podcast para María el viernes a las 16:00
🤖: ✅ ¡Reserva confirmada! ...
API (con curl)
bash
Copiar
Editar
curl -X POST "http://127.0.0.1:8000/reservar/" \
  -d "usuario=María" -d "fecha=14/06/2024" -d "hora=16:00" -d "tipo_servicio=Podcast"
📑 Licencia
Proyecto privado, uso interno Hermitage Agency.
Contáctanos para permisos de uso o contribución externa.

