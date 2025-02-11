import pandas as pd

# Crear DataFrame con datos ficticios
data = {
    "fecha": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "horas_trabajadas": [6, 7, 5, 8, 4, 6, 7, 8, 5, 6],
    "tareas_completadas": [3, 4, 2, 5, 1, 3, 4, 5, 2, 3]
}

df = pd.DataFrame(data)

# Guardar en CSV
df.to_csv("Ciencia-de-Datos-Productividad/ejercicios/datos_productividad.csv", index=False)
