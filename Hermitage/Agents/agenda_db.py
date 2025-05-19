import sqlite3

def init_db():
    conn = sqlite3.connect("agenda.db")
    c = conn.cursor()
    # Verifica si ya existe la columna tipo_servicio
    c.execute("PRAGMA table_info(reservas)")
    columns = [col[1] for col in c.fetchall()]
    if 'tipo_servicio' not in columns:
        # Si no existe, la agregas (para migraciones suaves)
        try:
            c.execute("ALTER TABLE reservas ADD COLUMN tipo_servicio TEXT")
        except sqlite3.OperationalError:
            pass  # Ya existe, ignore error
    c.execute("""
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY,
        usuario TEXT,
        fecha TEXT,
        hora TEXT,
        tipo_servicio TEXT
    )""")
    conn.commit()
    conn.close()


def disponible(fecha, hora, tipo_servicio):
    conn = sqlite3.connect("agenda.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reservas WHERE fecha=? AND hora=? AND tipo_servicio=?", (fecha, hora, tipo_servicio))
    libre = c.fetchone() is None
    conn.close()
    return libre


def reservar(usuario, fecha, hora, tipo_servicio):
    conn = sqlite3.connect("agenda.db")
    c = conn.cursor()
    c.execute("INSERT INTO reservas (usuario, fecha, hora, tipo_servicio) VALUES (?, ?, ?, ?)", (usuario, fecha, hora, tipo_servicio))
    conn.commit()
    conn.close()
    return True

