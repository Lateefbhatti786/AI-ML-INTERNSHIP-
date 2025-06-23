# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# checking  dataset
df = pd.read_csv('titanic.csv')
print("First 5 rows of the dataset:")
print(df.head())

# data information 
print("\nDataset Info:")
df.info()


# Checking for missing values
print("\nMissing Values:")
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]
print(missing_values)

# Visualizing missing values
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.show()

# Filling missing values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Dropping 'Cabin' column due to high number of missing values
df.drop(columns=['Cabin'], inplace=True)

# Converting categorical variables to numerical
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Initializing the scaler
scaler = StandardScaler()

# Scaling 'Age' and 'Fare' columns
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
plt.figure(figsize=(10, 5))
sns.histplot(df['Fare'], kde=True, bins=40, color='green', edgecolor='black', alpha=0.7)

# Mean line
mean_fare = df['Fare'].mean()
plt.axvline(mean_fare, color='red', linestyle='--', linewidth=2, label=f'Mean Fare = {mean_fare:.2f}')

# Title and axis labels
plt.title('Fare Distribution', fontsize=14)
plt.xlabel('Fare (Standardized)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Show legend and grid
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Final cleaned dataset info
print("\nCleaned dataset info:")
df.info()


# Save cleaned dataset to a new CSV
df.to_csv('cleaned_titanic.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_titanic.csv'")

