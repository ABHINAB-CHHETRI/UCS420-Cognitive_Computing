#Q1
import pandas as pd
data={
'T_Id':[1,2,3,4,5,6,7,8,9,10],
'Refund':['yes','no','no','yes','no','no','yes','no','no','no'],
'Marital_Status':['single','married','single','married','divorced','married','divorced',
'single','married','single'],
'Taxable_Income':['125K','100K','70K','120K','95K','60K','220K','85K','75K','90K'],
'Cheat':['NO','NO','NO','NO','YES','NO','NO','YES','NO','YES']
}
df=pd.DataFrame(data)
#Q2
print(df.iloc[0])
print(df.iloc[4])
print(df.iloc[7])
print(df.iloc[8])
#Q3
print(df.iloc[3:8])
print(df.iloc[4:9,2:5])
print(df.iloc[:,1:4])

#Q4
df = pd.read_csv('Iris.csv')
df.drop([4], inplace=True)
df.drop(df.columns[3],axis=1, inplace=True)
print(df.head())
