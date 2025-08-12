import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Titanic CSV file
df = pd.read_csv("titanic.csv")

# Step 2: Inspect data
print("First 10 rows of the dataset:")
print(df.head(10))

print("\nDataset Information:")
print(df.info())

# Step 3: Summary Statistics for numeric columns
print("\nSummary Statistics:")
print(df.describe())

# Step 4: Count missing values per column
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Step 5: Fill missing numeric values with the mean (example: Age)
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Step 6: Filter rows where Age > 30
filtered_df = df[df['Age'] > 30]

# Step 7: Sort the filtered data by Fare in descending order
sorted_df = filtered_df.sort_values(by='Fare', ascending=False)
print("\nFiltered and Sorted Data (Age > 30, sorted by Fare descending):")
print(sorted_df[['Name', 'Age', 'Fare']].head(10))

# Step 8: Group by 'Pclass' and calculate mean Fare
group_avg = df.groupby('Pclass')['Fare'].mean()
print("\nAverage Fare by Pclass:")
print(group_avg)

# Step 9: Visualization

# Histogram of Age
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.hist(df['Age'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('FREQUENCY')

# Bar chart of Average Fare by Pclass
plt.subplot(1,2,2)
group_avg.plot(kind='bar', color='orange')
plt.title('Average Fare by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Average Fare.')

plt.tight_layout()
plt.show()

# Step 10: Save cleaned dataset as processed_data.csv
df.to_csv("processed_data.csv", index=False)
print("\nCleaned data saved as 'processed_data.csv'.")
