import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #seaborn subpart of matplot
import warnings
warnings.filterwarnings('ignore')
#Reading data Detail study is in pandas section
#data_frame=pd.read_csv(path)
df=pd.read_csv("/home/krish/Downloads/Toyota.csv") #df=> Data Frame
print("Data loaded successfully")

#####################################################################

print(df.head()) #Display first 5 records

######################################################################

# sns.countplot(x='Price', data=df)
# print("\nSummary Statistics:")
# print(df.describe())
# plt.show()

####################################################################

# print(df.head()) #Display first 5 records
# print(df.tail()) #Display last 5 recordds
# df['Age'].plot.hist()
# plt.title('Histogram of Data')
# plt.show()

####################################################################

# df['Age'].plot.box() # detection of outler (extream min and max)
# plt.title('box plot of Data')
# plt.show()

######################################################################

# print(df['Price'].count()) 
# print(df['Price'].value_counts()) 

# ####################################################################

# df['Price'].value_counts().plot.bar() 
# plt.title('Gender bar Data')
# plt.show()

#######################################################################

# print(np.round(df["Age"].value_counts()/len(df["Age"])*100,2))

##################################### Bi- varient variable analysis ############################################################
# bi varient analysis is a analysis of two variable
# continuous - continuous 
# corr(), scatter()
# categorical - continous
# mean() and bar()
# categorical - categorical 
# chi square test

#########################################################################################################


######################################################################################################
# Scatter plot

# df.plot.scatter('Age','Price') # first value is dependent and second value of independent
# plt.show()

########################################################################################################

# mean = df.groupby('Price')['Age'].mean()
# print(type(mean))
# print(mean)

#####################################################################################################

# mean = df.groupby('Price')['Age'].mean().plot.bar()
# plt.show()

#################################################################################################
