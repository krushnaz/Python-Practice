import pandas as pd
import numpy as np

employee = {
    'EID' :[23201,20302,23203],
    'ENAME':['Shubham','Meera','Rohit'],
    'HRA':[4000,3000,2500],
    'TA':[3000,np.nan,3000],
    'DA':[8000,8500,8200]
}

df = pd.DataFrame(employee)

# sum of each column
column_sum = df.sum()
print("sum of each column :")
print(column_sum)

# count missing values from dataframe 
missing_val = df.isnull().sum().sum()
print("sum of all missing values :")
print(missing_val)

# Add column grossalary 
df['GrossSalary'] = df['HRA']+df['TA']+df['DA']
print(df)

# Display all column names 
print("columns :",df.columns.tolist())


