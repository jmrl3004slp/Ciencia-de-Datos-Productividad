import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect("Ciencia-de-Datos-Productividad/ejercicios/productividad.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS productividad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    actividad TEXT,
    horas_trabajadas REAL,
    tareas_completadas INTEGER
)
""")

conn.commit()
conn.close()

print("✅ ¡Base de datos y tabla creadas con éxito!")
