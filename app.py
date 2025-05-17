import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from herramientas_agenda import agendar_reserva
from agenda_db import init_db

init_db()

herramientas = [
    Tool(
        name="Agendar Coworking",
        func=agendar_reserva,
        description="Agenda espacios de coworking recibiendo nombre, fecha (dd/mm/aaaa) y hora (hh:mm) en español."
    )
]

llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
agente = initialize_agent(
    herramientas,
    llm,
    agent="zero-shot-react-description",
    verbose=False
)

st.title("🤖 Hermitage Chatbot de Reservas")
st.write("Solicita una reserva de coworking en español. Ejemplo: 'Reservar para Miguel el 20/05/2025 a las 10:00'.")

if 'historial' not in st.session_state:
    st.session_state.historial = []

entrada = st.text_input("Escribe tu mensaje:")

if entrada:
    respuesta = agente.run(entrada)
    st.session_state.historial.append(("Tú", entrada))
    st.session_state.historial.append(("Hermitage", respuesta))

for rol, msg in st.session_state.historial:
    if rol == "Tú":
        st.write(f"**Tú:** {msg}")
    else:
        st.write(f"**🤖 Hermitage:** {msg}")
