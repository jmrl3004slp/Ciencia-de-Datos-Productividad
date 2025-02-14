import pandas as pd

# Cargar datos desde el CSV
df = pd.read_csv("Ciencia-de-Datos-Productividad/ejercicios/datos_productividad.csv")

# Convertir columna 'Horas_Trabajadas' a numérico (manejo de NaN)
df["Horas_Trabajadas"] = pd.to_numeric(df["Horas_Trabajadas"], errors="coerce")

# Calcular métricas estadísticas
media = df["Horas_Trabajadas"].mean()
mediana = df["Horas_Trabajadas"].median()
moda = df["Horas_Trabajadas"].mode().values[0]
desviacion = df["Horas_Trabajadas"].std()

# Mostrar resultados
print(f"📊 Análisis Estadístico de Productividad:")
print(f"✅ Media: {media:.2f} horas")
print(f"✅ Mediana: {mediana:.2f} horas")
print(f"✅ Moda: {moda:.2f} horas")
print(f"✅ Desviación Estándar: {desviacion:.2f} horas")
