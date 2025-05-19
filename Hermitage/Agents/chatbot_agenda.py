from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from rich import print
from Hermitage.utils.herramientas_agenda import agendar_reserva
from Hermitage.utils.servicios_catalogo import SERVICIOS_CATALOGO
from Hermitage.agents.agenda_db import init_db
from dotenv import load_dotenv
load_dotenv()


def menu_admin():
    while True:
        print("\n[Admin] Opciones:")
        print("1. Listar reservas")
        print("2. Cancelar reserva")
        print("3. Volver")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            from Hermitage.utils.herramientas_agenda import mostrar_reservas
            mostrar_reservas()
        elif opcion == "2":
            from Hermitage.utils.herramientas_agenda import cancelar_reserva_cli
            cancelar_reserva_cli()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

def main():
    init_db()
    herramientas = [
        Tool(
            name=f"Agendar {servicio}",
            func=lambda query, tipo=servicio: agendar_reserva(query, tipo_servicio=tipo),
            description=f"Agenda {info['descripcion']}. Pide nombre, fecha (dd/mm/aaaa o natural) y hora (hh:mm o natural)."
        ) for servicio, info in SERVICIOS_CATALOGO.items()
    ]

    llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
    agente = initialize_agent(
        herramientas,
        llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    print("👋 Bienvenido al chatbot de reservas Hermitage. Servicios disponibles:")
    for s, info in SERVICIOS_CATALOGO.items():
        print(f"  - {s}: {info['descripcion']}")
    print("Escribe tu solicitud:")

    while True:
        mensaje = input("Tú: ")
        if mensaje.lower() in ['salir', 'exit', 'quit']:
            print("¡Hasta pronto!")
            break
        if mensaje.lower() in ['admin', 'menu', 'reservas']:
            menu_admin()
            continue
        respuesta = agente.run(mensaje)
        print("🤖:", respuesta)

if __name__ == "__main__":
    main()
