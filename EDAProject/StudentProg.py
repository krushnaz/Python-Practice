import pandas as pd
stud=pd.DataFrame({
    'Name':['Henry','John','David','Holmes','Marvin','Simon','Robert','Trent'],
    'Obedient':['Y','N','N','Y','N','Y','Y','Y'],
    'Grade':['A','C','F','B','E','A','B','C'],
    'ResearchScore':[90,85,10,75,20,92,60,75],
    'ProjectScore':[85,51,17,71,30,79,59,33],
    'Recommendation':['YES','YES','NO','NO','NO','YES','NO','NO']
})

stud.to_csv("student.csv")
student = pd.read_csv("student.csv")
# print(stud.head())

# print(stud[stud['ResearchScore'] < 70])

stud["Total"] = stud['ResearchScore'] + stud['ProjectScore']
# print(stud.head())

# def perc(total):
#     percentages = []
#     for t in total:
#         per = t / 200 * 100
#         percentages.append(per)
#     return percentages
# stud["Percentage"] = stud["Total"]/200*100
def calPerc(x) :
    return (x/200)*100
calPerc(185)
stud['percentage'] = round(stud['Total'].apply(calPerc))
# print(stud.head())
# print(stud.info())
stud1 = stud.select_dtypes(exclude='object')
# print(stud1)

stud["Total"] = stud["Total"].astype("float")
# stud.info()


# rename column percentage as a PER

stud = stud.rename(columns={'percentage': 'PER'})
# print(stud)

# droping column 
stud.drop(columns=['PER'], inplace=True)
# print(stud)

stud['percentage'] = stud["Total"]/200*100
# print(stud)

stud["New_Recommendation"] = stud["Recommendation"].map({"YES":1,"NO":0})
# print(stud)

# All rows and columns 
print(stud.iloc[:,:3])


# 1. Find statastic 
