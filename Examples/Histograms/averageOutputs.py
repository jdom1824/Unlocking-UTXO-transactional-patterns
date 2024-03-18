import pandas as pd
from tqdm import tqdm

# Leer el archivo CSV generado
df = pd.read_csv('full.csv')

# Convertir la columna 'Outputs' a tipo numérico para facilitar el cálculo
df['Outputs'] = pd.to_numeric(df['Outputs'])

# Calcular el tamaño total de cada transacción multiplicando el tamaño por el número de salidas
df['TotalSize'] = df['Size'] * df['Outputs']

# Calcular el crecimiento promedio por salida
df['AverageGrowthPerOutput'] = df['TotalSize'] / df['Outputs']

# Ordenar las transacciones por número de salidas y tamaño total
with tqdm(total=20, desc='Procesando') as pbar:
    most_outputs = df.sort_values(by='Outputs', ascending=False).head(10)
    pbar.update(10)
    heaviest_transactions = df.sort_values(by='TotalSize', ascending=False).head(10)
    pbar.update(10)

# Mostrar la tabla de transacciones con más salidas
print("Transacciones con más salidas:")
print(most_outputs[['Transaction', 'Outputs']])

# Mostrar la tabla de transacciones más pesadas
print("\nTransacciones más pesadas:")
print(heaviest_transactions[['Transaction', 'TotalSize']])

# Mostrar la tabla con el crecimiento promedio por salida
print("\nCrecimiento promedio por salida:")
print(df[['Transaction', 'AverageGrowthPerOutput']])
