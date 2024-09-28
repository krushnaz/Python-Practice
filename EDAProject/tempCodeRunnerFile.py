print(df.info())
print(df['Age'].fillna(np.round(df['Age'].mean)))