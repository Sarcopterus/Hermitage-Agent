import re
from datetime import datetime, timedelta
from .agenda_db import disponible, reservar




def interpretar_fecha(texto):
    texto = texto.lower()
    hoy = datetime.now()
    if "hoy" in texto:
        return hoy.strftime("%d/%m/%Y")
    if "mañana" in texto and "pasado" not in texto:
        return (hoy + timedelta(days=1)).strftime("%d/%m/%Y")
    if "pasado mañana" in texto:
        return (hoy + timedelta(days=2)).strftime("%d/%m/%Y")
    # Busca fechas explícitas tipo 20/05/2025 o 20-05-2025
    match_fecha = re.search(r'(\d{1,2}[/\-]\d{1,2}[/\-]\d{4})', texto)
    if match_fecha:
        return match_fecha.group(1)
    return None

def interpretar_hora(texto):
    texto = texto.lower()
    match_hora = re.search(r'(\d{1,2}:\d{2})', texto)
    if match_hora:
        return match_hora.group(1)
    match_hora_2 = re.search(r'(\d{1,2})\s*(am|pm)', texto)
    if match_hora_2:
        hora = int(match_hora_2.group(1))
        if match_hora_2.group(2) == 'pm' and hora < 12:
            hora += 12
        return f"{hora:02d}:00"
    return None

def agendar_reserva(query):
    usuario = "Invitado"
    match_nombre = re.search(r'para (\w+)', query.lower())
    if match_nombre:
        usuario = match_nombre.group(1).capitalize()

    fecha = interpretar_fecha(query)
    hora = interpretar_hora(query)

    if not fecha or not hora:
        return ("Por favor, indica la **fecha** y la **hora** de forma clara. "
                "Ejemplo: 'Reservar para Miguel el 20/05/2025 a las 10:00'.")

    # Validación de fecha pasada
    try:
        fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
        if fecha_dt < datetime.now():
            return "No puedes reservar en una fecha pasada. Elige una fecha futura."
    except:
        return "Formato de fecha incorrecto."

    if disponible(fecha, hora):
        reservar(usuario, fecha, hora)
        return f"¡Reserva confirmada para {usuario} el {fecha} a las {hora}!"
    else:
        return f"Lo siento, ese horario ya está reservado. ¿Te gustaría probar otra hora?"
