import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns #seaborn subpart of matplot
import warnings
warnings.filterwarnings('ignore')
#Reading data Detail study is in pandas section
#data_frame=pd.read_csv(path)
df=pd.read_csv("/home/krish/Downloads/train_titanic (2).csv") #df=> Data Frame
df.head() #Display first 5 records
#df.tail() #Display last 5 recordds'
plt.show()