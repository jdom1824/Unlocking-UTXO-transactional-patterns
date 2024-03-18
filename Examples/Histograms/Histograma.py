import pandas as pd
import matplotlib.pyplot as plt
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

# Create the histogram
plt.hist(df_filtered['Size'], bins=50, edgecolor='black', log=True) # log scale on y-axis
plt.title('Bitcoin Histogram of Transaction Sizes')
plt.xlabel('Transaction Size (MB) ')
plt.ylabel('Log(Number of Transactions)')
plt.grid(True)

# Save the figure as a .png file
plt.savefig('Histograma_full_2.png')
