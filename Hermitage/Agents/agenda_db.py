import sqlite3

def init_db():
    conn = sqlite3.connect("agenda.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY,
        usuario TEXT,
        fecha TEXT,
        hora TEXT
    )""")
    conn.commit()
    conn.close()

def disponible(fecha, hora):
    conn = sqlite3.connect("agenda.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reservas WHERE fecha=? AND hora=?", (fecha, hora))
    libre = c.fetchone() is None
    conn.close()
    return libre

def reservar(usuario, fecha, hora):
    conn = sqlite3.connect("agenda.db")
    c = conn.cursor()
    c.execute("INSERT INTO reservas (usuario, fecha, hora) VALUES (?, ?, ?)", (usuario, fecha, hora))
    conn.commit()
    conn.close()
    return True
