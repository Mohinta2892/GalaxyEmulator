import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the data

# Create DataFrame for easier analysis
input_columns = ['Omega_m', 'A_s', 'w0', 'h', 'z', 'c_min']
df_inputs = pd.DataFrame(inputs, columns=input_columns)

# Basic statistical summary
print("Statistical Summary:")
print(df_inputs.describe())

# Correlation Matrix
plt.figure(figsize=(10, 8))
correlation_matrix = df_inputs.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Input Variables Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

# Pairplot for visualizing relationships
sns.pairplot(df_inputs)
plt.suptitle('Pairplot of Input Variables', y=1.02)
plt.savefig('pairplot.png')
plt.close()

# Distribution of variables
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.ravel()
for i, col in enumerate(input_columns):
    sns.histplot(df_inputs[col], kde=True, ax=axes[i])
    axes[i].set_title(f'Distribution of {col}')
plt.tight_layout()
plt.savefig('distributions.png')
plt.close()

# Print additional insights
print("\nCorrelation Matrix:")
print(correlation_matrix)
