import pandas as pd
import sqlite3

# Leer datos desde el CSV
df = pd.read_csv("Ciencia-de-Datos-Productividad/ejercicios/datos_productividad.csv")

# Conectar a la base de datos
conn = sqlite3.connect("Ciencia-de-Datos-Productividad/ejercicios/productividad.db")
cursor = conn.cursor()

# Insertar datos fila por fila
for _, row in df.iterrows():
    cursor.execute("""
    INSERT INTO productividad (fecha, actividad, horas_trabajadas, tareas_completadas) 
    VALUES (?, ?, ?, ?)
    """, (row["Fecha"], row["Actividad"], row["Horas_Trabajadas"], row["Tareas_Completadas"]))

conn.commit()
conn.close()

print("✅ ¡Datos insertados correctamente en la base de datos!")
