import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
filepath = '../data/insurance_data.csv'
data = pd.read_csv(filepath)

# Data Overview
print(data.info())
print(data.describe())
print(data.head())

# Missing Values
print("Missing Values:\n", data.isnull().sum())

# Univariate Analysis
plt.figure(figsize=(10, 6))
sns.histplot(data['TotalPremium'], kde=True, bins=30)
plt.title('Distribution of Total Premium')
plt.savefig('../visualizations/total_premium_distribution.png')
plt.show()

# Bivariate Analysis - Total Claims vs Total Premium
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TotalPremium', y='TotalClaims', data=data)
plt.title('Total Claims vs Total Premium')
plt.savefig('../visualizations/premium_vs_claims.png')
plt.show()

# Correlation Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('../visualizations/correlation_matrix.png')
plt.show()
