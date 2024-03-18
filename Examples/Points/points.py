# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from tqdm import tqdm

data = []
patterns = {'splitting': [], 'merging': [], 'transferring': []}

with open('/home/juandavid/Dunas/full/full.csv', 'r') as file:
    for line in file.readlines()[1:]:
        item = line.strip().split(',')
        if len(item) >= 4:
            size = int(item[1])
            inputs = int(item[2])
            outputs = int(item[3])

            if inputs < outputs:
                patterns['splitting'].append((size, inputs))
            elif inputs > outputs:
                patterns['merging'].append((size, inputs))
            else:
                patterns['transferring'].append((size, inputs))

print("Cargacompleta")
# Get the counts of each pattern
counts = {pattern: len(value) for pattern, value in patterns.items()}  # Corrected data to value

# Progress bar
pbar = tqdm(total=sum(counts.values()), desc='Processing data', dynamic_ncols=True)

# Define colors for each pattern
colors = {'splitting': 'red', 'merging': 'blue', 'transferring': 'green'}

# Plot the scatter points for each pattern
for pattern, data in patterns.items():
    fig, ax = plt.subplots()  # Create a new figure for each pattern
    sizes, input_counts = zip(*data)
    ax.scatter(sizes, input_counts, c=colors[pattern], s=5, label=pattern)  # Added label for legend
    pbar.update(len(data))  # Update the progress bar

    # Customize the axes and add labels
    ax.set_xlabel('Size')
    ax.set_ylabel('Number of Outputs')  # Update y-axis label
    ax.set_title(f'{pattern}')  # Updated to use pattern
    #ax.legend()  # Add legend

    # Adjust the aspect ratio of the axes
    ax.set_aspect('auto')
    plt.grid(True)
    
    # Save each plot as a separate PNG file
    plt.savefig(f'{pattern}_points.png')

# Close the progress bar
pbar.close()
