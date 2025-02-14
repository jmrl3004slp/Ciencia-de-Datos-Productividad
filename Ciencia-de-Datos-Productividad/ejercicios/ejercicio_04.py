import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos desde el CSV
df = pd.read_csv("Ciencia-de-Datos-Productividad/ejercicios/datos_productividad.csv")

# Convertir la columna de fecha a formato datetime
df["Fecha"] = pd.to_datetime(df["Fecha"])

# Graficar la evolución de las horas trabajadas
plt.figure(figsize=(10, 5))
sns.lineplot(x="Fecha", y="Horas_Trabajadas", data=df, marker="o", label="Horas Trabajadas")
plt.xticks(rotation=45)
plt.title("Tendencia de Horas Trabajadas")
plt.xlabel("Fecha")
plt.ylabel("Horas")
plt.legend()
plt.show()

# Graficar la cantidad de tareas completadas
plt.figure(figsize=(10, 5))
sns.barplot(x="Fecha", y="Tareas_Completadas", data=df, palette="Blues")
plt.xticks(rotation=45)
plt.title("Tareas Completadas por Día")
plt.xlabel("Fecha")
plt.ylabel("Tareas")
plt.show()
