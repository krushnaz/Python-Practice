import pandas as pd 

# df = pd.read_csv("QP_Practice/student.csv")
# print(df.head(5))

# print("columns :",df.columns.tolist())

data = { 
    'rollNo':[11,12,13,14,15],
    'marks':[60,50,70,None,None]
        }

df = pd.DataFrame(data)
rows = len(df)
print("row count :")
print(rows)

countMissingVal = df.isnull().sum().sum()
print("missing values :")
print(countMissingVal)

col = len(df.columns)
print("column count :")
print(col)