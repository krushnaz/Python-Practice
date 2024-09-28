import numpy as np
import pandas as pd

# ======================Series====================================

# arr1 = np.array([10,20,30,40,50])
# si = pd.Series(arr1)
# print(si)

# data = [10,20,30,40,50]
# index = ['a','b','c','d','e']
# si = pd.Series(data,index)
# print(si)

# dictionary = {'a' : 10, 'b':20,'c':30,'d':40,'e':50}
# sd = pd.Series(dictionary)
# print(sd)

# ndarr = [[10,20,30],[40,50,60]]
# series = pd.Series(ndarr)
# print(series)


# ====================Data Frame =====================


# li = [1,2,3,4,5,6]
# df = pd.DataFrame(li)
# print(df)

# =====================
# Using data series
# =====================

# s1 = pd.Series([1,2,3])
# s2 = pd.Series([70.60,80.40,50.20])
# s3 = pd.Series(["vijay","sujay","santosh"])

# data = {"RollID":s1,"Marks":s2,"Name":s3}
# dseries = pd.DataFrame(data);
# print(dseries)

# =================
# Using dictionary
# =================

# dicts = {"name":['vijay',"sujay","krushna","omkar"],"marks":[80,40,90,95]}
# df = pd.DataFrame(dicts);
# print(df)

# =====================
# Using 2D numpy array
# =====================

# d1 = [[1,2,3,4],[5,6,7,8,9]]
# d2 = [[11,12,13,14],[15,16,17,18,19]]
# data = {"first":d1,"second":d2}
# df = pd.DataFrame(data)
# print(df)

# ========================Panel========================================
# =========================
# use panel data structure
# =========================
# info = np.random.rand(1,2,3)
# pd_panel = pd.Panel(info);
# print(pd_panel)

# it is deprecated data structure in pandas--- not working---

# ============
# Index Object
# ============

# idx = pd.Index(['mumbai','thane','pune','jalgaon','nagpur'])
# print(idx)
# result = idx.values
# print(result)

# ================
# Set_index Method
#=================
# df = pd.DataFrame({"fruits":["mango","banana","custedapple"],"price":[30,40,50]})
# print(df) 
# df = df.set_index(['fruits','price'])
# print(df)


# =========
# reindex
# =========
# df = pd.DataFrame({"fruits":["mango","banana","custedapple"],"price":[30,40,50]})
# print(df) 
# df = df.set_index(['fruits','price'])
# print(df)
# df = df.reset_index(['fruits','price'])
# print(df)

# =======================Drop Entry, Selecting Entry============================


# ======
# Drop()
# ======

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }
# df = pd.DataFrame(details,columns = ['Name','Age','City'],index=['a','b','c','d'])
# print(df)
# print()
# new_df = df.drop('c')
# print(new_df)

# ----------------------------------delete column by column name--------------------------------------------------
# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }
# df = pd.DataFrame(details,columns = ['Name','Age','City'],index=['a','b','c','d'])
# print(df)
# print()
# new_df = df.drop('City',axis=1)
# print(new_df)

# -------------------------------delete column by column name ------------------------------------------------------
# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }
# df = pd.DataFrame(details,columns = ['Name','Age','City'],index=['a','b','c','d'])
# print(df)
# print()
# new_df = df.drop('Age',axis=1)
# print(new_df)

# ------------------------------Delete column by column number ---------------------------------------

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }
# df = pd.DataFrame(details,columns = ['Name','Age','City'],index=['a','b','c','d'])
# print(df)
# print()
# new_df = df.drop(columns=df.columns[1])
# print(new_df)

#=======================
#delete column using Del  
# ======================

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }
# df = pd.DataFrame(details,columns = ['Name','Age','City'],index=['a','b','c','d'])
# print(df)
# print()
# del df['Name']
# print(df)

# ========================
# Add new row in dataframe
# ========================

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }
# df = pd.DataFrame(details,columns = ['Name','Age','City'],index=['a','b','c','d'])
# print(df)
# df.loc[len(df.index)] = ['ajay',50,"pune"]
# print(df)

# =========
# concat()
# =========

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }
# df1 = pd.DataFrame(details,columns = ['Name','Age','City'],index=['a','b','c','d'])
# print(df1)

# details = {'Name':['Yogita','Saniya','Ishita','Radha'],
#            'Age':[21,22,22,24],
#            'City':['Pune','Mumbai','Nashik','ch.Sambhajinagar']
#            }
# df2 = pd.DataFrame(details,columns = ['Name','Age','City'],index=['a','b','c','d'])
# print(df2)

# df3 = pd.concat([df1,df2],ignore_index=True)
# print(df3)


# ==========================Diffrent ways to add column in dataframe ==================================
# add column using list
# =====================

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }

# columns = ['Name','Age','City']
# index=['a','b','c','d']
# df = pd.DataFrame(details,columns = columns,index = index)

# print(df)
# print()
# # adding new column in to existing df
# dept = ['CO','EJ','IF','CO']
# df['dept'] = dept;
# print(df)

# ========
# Insert()
# ========
# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }

# columns = ['Name','Age','City']
# index=['a','b','c','d']
# df = pd.DataFrame(details,columns = columns,index = index)

# print(df)
# print()
# # adding new column using insert()
# dept = ['CO','EJ','IF','CO']
# df.insert(2,'Dept',dept,True)
# print(df)

# ========
# assign()
# ========

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }

# columns = ['Name','Age','City']
# index=['a','b','c','d']
# df = pd.DataFrame(details,columns = columns,index = index)

# print(df)
# print()
# # adding new column in to existing df
# df1 = df.assign(Dept = ['CO','EJ','IF','CO'])
# print(df1)

# =============================Selecting Entries ============================================

# ==========================================
# Selecting single column using column_name
# ==========================================

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }

# columns = ['Name','Age','City']
# index=['a','b','c','d']
# df = pd.DataFrame(details,columns = columns,index = index)
# print(df)

# df1 = df[['Name','Age']]
# print(df1)

# ==============================
# Selecting rows using condition
# ==============================

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }

# columns = ['Name','Age','City']
# index=['a','b','c','d']
# df = pd.DataFrame(details,columns = columns,index = index)

# sel = df.loc[df['Age']>22]
# print(sel)


# ===========================
# Multiple values using (|)
# ===========================

# details = {'Name':['Krushna','Aditya','Sangram','shubham'],
#            'Age':[21,22,22,24],
#            'City':['Ahilyanagar','Ahilyanagar','Sangli','Latur']
#            }

# columns = ['Name','Age','City']
# index=['a','b','c','d']
# df = pd.DataFrame(details,columns = columns,index = index)

# sel = df.loc[(df['City']== 'Ahilyanagar') |(df['City']== 'Latur')]
# print(sel)


# ========================== Data Alignment, Ranker and Sort =======================================


















