import dateparser
from Hermitage.agents.agenda_db import reservar, disponible
from Hermitage.utils.servicios_catalogo import SERVICIOS_CATALOGO
from datetime import datetime

def agendar_reserva(query, tipo_servicio):
    if tipo_servicio not in SERVICIOS_CATALOGO:
        return "⛔ Este servicio no está disponible actualmente."

    print(f"\nPara reservar {tipo_servicio}, necesito tus datos:")
    nombre = input("Nombre del usuario: ").strip()
    fecha_input = input("Fecha (ej. 'mañana', '15/06/2024'): ").strip()
    hora_input = input("Hora (ej. '15:00', '3pm'): ").strip()

    fecha_hora_dt = dateparser.parse(f"{fecha_input} {hora_input}", languages=["es"])
    if not fecha_hora_dt:
        return "❌ No pude entender la fecha y hora. Usa un formato válido o lenguaje natural sencillo."

    if fecha_hora_dt < datetime.now():
        return "❌ No puedes reservar en el pasado. Por favor elige una fecha/hora válida."

    fecha_str = fecha_hora_dt.strftime("%d/%m/%Y")
    hora_str = fecha_hora_dt.strftime("%H:%M")

    if not disponible(fecha_str, hora_str, tipo_servicio):
        return f"⛔ Ese horario ya está reservado para {tipo_servicio}. Intenta con otra hora/fecha."

    reservar(nombre, fecha_str, hora_str, tipo_servicio)
    return (f"✅ ¡Reserva confirmada!\n"
            f"- Servicio: {tipo_servicio}\n"
            f"- Usuario: {nombre}\n"
            f"- Fecha: {fecha_str}\n"
            f"- Hora: {hora_str}")

def mostrar_reservas():
    from Hermitage.agents.agenda_db import listar_reservas
    reservas = listar_reservas()
    if not reservas:
        print("No hay reservas registradas.")
        return
    print("\nReservas actuales:")
    for r in reservas:
        print(f"ID: {r[0]} | Usuario: {r[1]} | Fecha: {r[2]} | Hora: {r[3]} | Servicio: {r[4]}")

def cancelar_reserva_cli():
    from Hermitage.agents.agenda_db import cancelar_reserva, listar_reservas
    mostrar_reservas()
    id_reserva = input("Ingresa el ID de la reserva que quieres cancelar: ").strip()
    if not id_reserva.isdigit():
        print("ID inválido.")
        return
    ok = cancelar_reserva(int(id_reserva))
    if ok:
        print(f"Reserva ID {id_reserva} cancelada exitosamente.")
    else:
        print("No se pudo cancelar la reserva. Verifica el ID.")
