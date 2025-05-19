from fastapi import FastAPI, HTTPException
from Hermitage.agents.agenda_db import reservar, disponible, listar_reservas, cancelar_reserva

app = FastAPI(title="Hermitage Agenda API")

@app.post("/reservar/")
def reservar_api(usuario: str, fecha: str, hora: str, tipo_servicio: str):
    if not disponible(fecha, hora, tipo_servicio):
        raise HTTPException(status_code=409, detail="Ese horario ya está reservado.")
    reservar(usuario, fecha, hora, tipo_servicio)
    return {"msg": "Reserva exitosa"}

@app.get("/reservas/")
def listar_api():
    return {"reservas": listar_reservas()}

@app.delete("/reservar/{reserva_id}/")
def cancelar_api(reserva_id: int):
    cancelar_reserva(reserva_id)
    return {"msg": "Reserva cancelada"}
