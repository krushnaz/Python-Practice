# predictive modeling invloves six deffrent 
# 1.problem defination 
# 2.hypothesis genration
# 3.data extraction and collection
# 4.data exploration and tranformation 
# 5.model building 
# 6.model deployement and implementation 
# CSV -> comma separated file


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #seaborn subpart of matplot
import warnings
warnings.filterwarnings('ignore')
#Reading data Detail study is in pandas section
#data_frame=pd.read_csv(path)
df=pd.read_csv("/home/krish/Downloads/train_titanic (2).csv") #df=> Data Frame
# print("Data loaded successfully")
# sns.countplot(x='Survived', data=df)
# print("\nSummary Statistics:")
# print(df.describe())
# plt.show()
# print(df.head()) #Display first 5 records
# print(df.tail()) #Display last 5 recordds
# df['Age'].plot.hist()
# plt.title('Histogram of Data')
# plt.show()

# df['Age'].plot.box() # detection of outler (extream min and max)
# plt.title('box plot of Data')
# plt.show()

# print(df['Gender'].count()) 
# print(df['Gender'].value_counts()) 

# df['Gender'].value_counts().plot.bar() 
# plt.title('Gender bar Data')
# plt.show()

# print(np.round(df["Gender"].value_counts()/len(df["Gender"])*100,2))

##################################### Bi- varient variable analysis ############################################################
# bi varient analysis is a analysis of two variable
# continuous - continuous 
# corr(), scatter()
# categorical - continous
# mean() and bar()
# categorical - categorical 
# chi square test

# print(df['Age'].corr(df['Fare']))  # 0.09606669176903888  fare => target && Age => predicator
#  if near to 1 then strong bond => positive effect

# Scatter plot

# df.plot.scatter('Age','Fare') # first value is dependent and second value of independent
# plt.show()

# mean = df.groupby('Gender')['Age'].mean()
# print(type(mean))
# print(mean)

# mean = df.groupby('Gender')['Age'].mean().plot.bar()
# plt.show()

# from scipy.stats import ttest_ind
# male = df[df['Gender'] == 'Male']
# female = df[df['Gender'] == 'Female']
# ttest_ind(male['Age'],female['Age'],nan_policy ='omit')
# print(pd.crosstab(df['Gender'],df['Survived']))

# 
# print(df.isnull().sum())
# print(df.sum())
# print(np.round(df['Age'].mean()))

# print(df.info())
# print(df['Age'].fillna(np.round(df['Age'].mean)))

# print(df['Cabin'].mode())
# print(df['Cabin'].value_counts())

# print(df['Cabin'].fillna(
#     df['Cabin'].value_counts().index(0), inplace=True
# ),df['Cabin'].value_counts())

# sns.countplot(x='Survived',hue='Gender',data=df)
# plt.show()
