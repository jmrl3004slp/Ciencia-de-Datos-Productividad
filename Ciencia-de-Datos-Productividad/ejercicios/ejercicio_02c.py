import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("Ciencia-de-Datos-Productividad/ejercicios/productividad.db")
cursor = conn.cursor()

# Obtener los primeros registros
cursor.execute("SELECT * FROM productividad LIMIT 5")
rows = cursor.fetchall()

conn.close()

# Mostrar resultados
for row in rows:
    print(row)
