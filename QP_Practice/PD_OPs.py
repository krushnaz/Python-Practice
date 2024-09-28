import pandas as pd

data = {
    'City' : ['Dilhi','Bangoluru','Chainai','Mumbai','Kolkata'],
    'MaxTemp' : [40,31,35,29,39],
    'MinTemp' :[32,25,27,21,23],
    'RainFall' :[24.1,36.2,40.8,35.2,41.8]
}
# 1. read csv.file and create dataframe
df = pd.DataFrame(data)
# print(df)

# 2. Display no of rows and column
row, column = df.shape
print("no of rows :",row)
print("no of column :",column)

# 3. Display all columns name

print(df.columns.tolist())

# 4. Compute mean of column rainfall 
mean = df['RainFall'].mean()
print("mean of RainFall column :",mean)

# 5. compute meadian of the MaxTemp column 

median = df['MaxTemp'].median()
print("median of MaxTemp column :",median)

# 6. Display name of the cities having 'MinTemp > 25'
name_of_cities = df[df['MinTemp'] > 25]['City'].tolist()
print("Cities with mean temp > 25 :",name_of_cities)

# 7. Sort RainFall column and Display Information 
sorted_df = df.sort_values(by="RainFall")
print("Sorted RainFall :")
print(sorted_df)