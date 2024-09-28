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
csv_file = df.to_csv("Employee.csv")

df = pd.read_csv('./Employee.csv')
print(df)
# Indexing and Selection:
select_many = df[['ENAME','DA']]
print(select_many)

dfLoc = df.loc[1]
print(dfLoc)


