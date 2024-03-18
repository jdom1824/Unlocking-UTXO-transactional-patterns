# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the database from the text file
df = pd.read_csv('/home/juandavid/Dunas/Ten_percent/30_percent_transactions.csv', sep=',', header=0, names=['Transaction', 'Size', 'Inputs', 'Outputs', 'Block'], 
                 converters={'Size': lambda x: int(x)}, 
                 iterator=True, chunksize=1000)

# Concatenate chunks into one DataFrame
df = pd.concat(df, ignore_index=True)

# No conversion from bytes to MB this time
df_filtered = df[df['Size'] <= 1e6]  # Note that now 1Mb is 1e6 bytes

# Define size categories based on percentiles
percentiles = list(np.percentile(df_filtered['Size'], np.arange(0, 100, 20))) # Change 20 to another number to adjust the number of categories
percentiles.append(df_filtered['Size'].max())
size_bins = pd.cut(df_filtered['Size'], bins=percentiles, include_lowest=True)

# Count the number of transactions per size category
df_grouped = df_filtered.groupby(size_bins).size().reset_index(name='Counts')

# Define labels
labels = ['{}-{} Bytes'.format(int(a), int(b)) for a, b in zip(percentiles[:-1], percentiles[1:])]

# Define explode
explode = [0.1] * len(df_grouped['Counts'])

# Create a pie chart
plt.pie(df_grouped['Counts'], labels = labels, autopct='%1.1f%%', explode=explode)

# Add title with total number of transactions
plt.title('Distribution of Transaction Sizes (Total Transactions: {})'.format(df_filtered.shape[0]))

# Display the plot
plt.savefig('Torta_full.png')
