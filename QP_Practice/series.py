import pandas as pd

# Create Series for account number, name, and balance
account_number = pd.Series([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
name = pd.Series(['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry'])
balance = pd.Series([5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000])

# Create DataFrame using the Series
df = pd.DataFrame({'Account Number': account_number, 'Name': name, 'Balance': balance})

# Display the DataFrame
print(df)
