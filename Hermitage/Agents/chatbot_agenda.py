from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from rich import print  # pip install rich
from Hermitage.utils.herramientas_agenda import agendar_reserva
from Hermitage.utils.agenda_db import init_db


def main():
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
        verbose=True
    )

    print("👋 Bienvenido al chatbot de reservas de coworking Hermitage. Escribe tu solicitud:")
    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() in ['salir', 'exit', 'quit']:
            print("¡Hasta pronto!")
            break
        respuesta = agente.run(mensaje)
        print("🤖:", respuesta)
if __name__ == "__main__":
    main()
