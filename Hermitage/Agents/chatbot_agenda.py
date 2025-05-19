from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from rich import print
from Hermitage.utils.herramientas_agenda import agendar_reserva
from Hermitage.agents.agenda_db import init_db

def main():
    init_db()
    herramientas = [
    Tool(
        name="Agendar Live Stream",
        func=lambda query: agendar_reserva(query, tipo_servicio="Live Stream"),
        description="Agenda el Set Live Stream (COP $200,000 por 2h). Pide nombre, fecha (dd/mm/aaaa) y hora (hh:mm)."
    ),
    Tool(
        name="Agendar Podcast",
        func=lambda query: agendar_reserva(query, tipo_servicio="Podcast"),
        description="Agenda el Set de Podcast (COP $400,000 por 2h). Pide nombre, fecha (dd/mm/aaaa) y hora (hh:mm)."
    ),
    Tool(
        name="Agendar Fotografía",
        func=lambda query: agendar_reserva(query, tipo_servicio="Fotografía"),
        description="Agenda el Set de Fotografía (COP $200,000 por 2h). Pide nombre, fecha (dd/mm/aaaa) y hora (hh:mm)."
    )
]

    llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
    agente = initialize_agent(
        herramientas,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    print("👋 Bienvenido al chatbot de reservas Hermitage. Puedes agendar: Live Stream, Podcast o Fotografía. Escribe tu solicitud:")
    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() in ['salir', 'exit', 'quit']:
            print("¡Hasta pronto!")
            break
        respuesta = agente.run(mensaje)
        print("🤖:", respuesta)

if __name__ == "__main__":
    main()
