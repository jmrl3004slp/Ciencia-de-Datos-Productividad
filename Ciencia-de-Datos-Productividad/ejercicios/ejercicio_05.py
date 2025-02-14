import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("Ciencia-de-Datos-Productividad/ejercicios/productividad.db")
cursor = conn.cursor()

# Obtener los días con más horas trabajadas
cursor.execute("""
SELECT fecha, horas_trabajadas FROM productividad
ORDER BY horas_trabajadas DESC
LIMIT 5
""")
top_horas = cursor.fetchall()
print("📊 Días con más horas trabajadas:")
for row in top_horas:
    print(row)

# Obtener el promedio de horas trabajadas
cursor.execute("SELECT AVG(horas_trabajadas) FROM productividad")
promedio_horas = cursor.fetchone()[0]
print(f"\n✅ Promedio de horas trabajadas: {promedio_horas:.2f}")

# Obtener los días con menos tareas completadas
cursor.execute("""
SELECT fecha, tareas_completadas FROM productividad
ORDER BY tareas_completadas ASC
LIMIT 5
""")
min_tareas = cursor.fetchall()
print("\n📉 Días con menos tareas completadas:")
for row in min_tareas:
    print(row)

conn.close()
