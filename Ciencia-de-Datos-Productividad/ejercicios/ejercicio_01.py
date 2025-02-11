import pandas as pd

# Crear DataFrame con datos ficticios
# Datos estáticos para 10 días (ajústalos según tu necesidad)
datos = [
    ["2024-02-01", "Trabajo", 8, 4],
    ["2024-02-02", "Trabajo", 7, 5],
    ["2024-02-03", "Scouts", None, None],  # Sábado
    ["2024-02-04", "Scouts", None, None],  # Domingo
    ["2024-02-05", "Trabajo", 6, 4],
    ["2024-02-06", "Trabajo", 8, 6],
    ["2024-02-07", "Trabajo", 7, 4],
    ["2024-02-08", "Trabajo", 9.5, 5],
    ["2024-02-09", "Trabajo", 6, 4],
    ["2024-02-10", "Scouts", None, None],  # Sábado
]
df = pd.DataFrame(datos, columns=["Fecha", "Actividad", "Horas_Trabajadas", "Tareas_Completadas"])

# Guardar en CSV
df.to_csv("Ciencia-de-Datos-Productividad/ejercicios/datos_productividad.csv", index=False)
