import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Datos
nodes = [7362, 7701, 8214, 8369, 9026, 9114, 9465, 11351, 11679, 12483, 8426, 7701, 5521, 3701, 2469, 2545, 1981]
storage = [1236, 1463, 1724.94, 1975.084, 2355.786, 2752.428, 3511.515, 5187.407, 5594.241, 6166.602, 4448.928, 4397.271, 3930.952, 3279.086, 2469, 2832.585, 2345.504]

# Invertir el orden de los datos
nodes = nodes[::-1]
storage = storage[::-1]

# Crear DataFrame desde los datos
df = pd.DataFrame({'Nodes': nodes, 'Storage': storage})

# Para evitar la suma del almacenamiento, hacemos que cada nodo sea único añadiendo un número de índice
df['Nodes'] = df['Nodes'].astype(str) + '_' + df.index.astype(str)

# Calcular la tasa de crecimiento y marcar el crecimiento exponencial
df['Growth'] = df['Storage'].pct_change()
df['Exponential'] = False
df.loc[len(df)-8:, 'Exponential'] = True  # Marcar las últimas 8 barras como crecimiento exponencial

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(12, 6))

# Determinar el ancho de las barras y el espaciado entre ellas
bar_width = 0.4
spacing = 0.1

# Generar gráfico de barras con colores personalizados
for i, (_, row) in enumerate(df.iterrows()):
    if row['Exponential']:
        color = 'salmon'
    else:
        color = 'dodgerblue'
    ax.bar(i, row['Storage'], width=bar_width, color=color, edgecolor='black', linewidth=0.7, align='center')

start_index = 9  # Inicia en la séptima barra
end_index = 17   # Termina en la decimosexta barra
ax.plot(range(start_index, end_index), df['Storage'][start_index:end_index], color='red', linewidth=2, marker='o')


# Configurar título y etiquetas
ax.set_title('Bar Chart of Nodes vs Storage')
ax.set_xlabel('Nodes')
ax.set_ylabel('Storage (TB)')

# Establecer las ubicaciones y etiquetas del eje x sin el índice
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df['Nodes'].str.split('_').str[0])

# Invertir el eje x
ax.invert_xaxis()

# Rotar las etiquetas del eje x para una mejor lectura
plt.xticks(rotation=45)

# Mostrar gráfico
plt.tight_layout()
plt.show()
