import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

# tqdm wrapper for pandas
tqdm.pandas()

# Load the database from the text file
df = pd.read_csv('full.csv', sep=',', header=0, names=['Transaction', 'Size', 'Inputs', 'Outputs', 'Block'], 
                 converters={'Size': lambda x: int(x)}, 
                 iterator=True, chunksize=1000)

# Concatenate chunks into one DataFrame
df = pd.concat(df, ignore_index=True)

df['Size'] = df['Size'] / 1e6  # Convert size from bytes to MB
df_filtered = df[df['Size'] <= 1]  # Note that now 1Mb is 1MB

# Count the number of transactions per block and size
df_grouped = df_filtered.groupby(['Block', 'Size']).size().reset_index(name='Counts')

# Creamos la figura
fig = plt.figure()

# Agregamos un plano 3D
ax = fig.add_subplot(111, projection='3d')

# Datos en array bi-dimensional
x = np.array(df_grouped['Block'])
y = np.array(df_grouped['Size'])
z = np.array(df_grouped['Counts']) # Number of Transactions
ax.scatter(x, y, z)

# Ponemos etiquetas
ax.set_xlabel('Block')
ax.set_ylabel('Transaction Size (MB)')
ax.set_zlabel('Number of Transactions')

# Mostramos el gráfico
plt.savefig('3d.png')
