import re
import dateparser
from Hermitage.agents.agenda_db import reservar, disponible
from Hermitage.utils.servicios_catalogo import SERVICIOS_CATALOGO
from datetime import datetime

def agendar_reserva(query, tipo_servicio):
    if tipo_servicio not in SERVICIOS_CATALOGO:
        return "⛔ Este servicio no está disponible actualmente."

    # Intentar extraer datos con regex básica
    # Nombre: después de "para"
    nombre_match = re.search(r"para\s+([A-Za-zÁÉÍÓÚáéíóúñÑ]+)", query, re.IGNORECASE)
    nombre = nombre_match.group(1) if nombre_match else None

    # Fecha: dd/mm/yyyy, dd-mm-yyyy o palabras clave
    fecha_match = re.search(r"(\d{1,2}[/\-]\d{1,2}[/\-]\d{4}|hoy|mañana|pasado mañana)", query, re.IGNORECASE)
    fecha_input = fecha_match.group(1) if fecha_match else None

    # Hora: hh:mm, h am/pm, hhmm, etc.
    hora_match = re.search(r"(\d{1,2}[:.]\d{2})|(\d{1,2}\s*(am|pm))", query, re.IGNORECASE)
    hora_input = None
    if hora_match:
        hora_input = hora_match.group(0)
    else:
        # Intentar también hh:mm sin espacio
        hora_match2 = re.search(r"\b(\d{1,2})\b", query)
        if hora_match2:
            hora_input = hora_match2.group(1) + ":00"

    if not nombre or not fecha_input or not hora_input:
        return (
            "❌ Por favor, especifica el **nombre**, la **fecha** y la **hora** en el mismo mensaje.\n"
            "Ejemplo: 'Reservar Podcast para María el 24/05/2025 a las 16:00'"
        )

    fecha_hora_dt = dateparser.parse(f"{fecha_input} {hora_input}", languages=["es"])
    if not fecha_hora_dt:
        return "❌ No pude entender la fecha y hora. Usa un formato válido."

    if fecha_hora_dt < datetime.now():
        return "❌ No puedes reservar en el pasado. Elige una fecha/hora válida."

    fecha_str = fecha_hora_dt.strftime("%d/%m/%Y")
    hora_str = fecha_hora_dt.strftime("%H:%M")

    if not disponible(fecha_str, hora_str, tipo_servicio):
        return f"⛔ Ese horario ya está reservado para {tipo_servicio}. Intenta con otra hora/fecha."

    reservar(nombre, fecha_str, hora_str, tipo_servicio)
    return (
        f"✅ ¡Reserva confirmada!\n"
        f"- Servicio: {tipo_servicio}\n"
        f"- Usuario: {nombre}\n"
        f"- Fecha: {fecha_str}\n"
        f"- Hora: {hora_str}"
    )

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
