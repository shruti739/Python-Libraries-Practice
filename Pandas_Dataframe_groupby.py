import pandas as pd 

Name = ['Virat','Hardik','Nayana','Laximi','Sony','Rohit']
gender = ['M','M','F','F','F','M']
Course = ['python','java','python','java','python','java']
fee = [35000,45000,12000,89000,77000,55500]

df=pd.DataFrame({'Student_name':Name,'Gender':gender,"Course":Course,"Fee":fee})

print(df)
print()
print(df.groupby("Course").sum())   # groups by course and prints the total fee. -  show complete data 
print(df.groupby("Course")["Fee"].sum())        # group by course and just total fee 
print(df.groupby("Course")["Fee"].count())
print(df.groupby("Course")["Fee"].max())        # prints the highest fee of each group by course
print(df.groupby("Course")["Fee"].min())        
print(df.groupby("Course")["Fee"].mean())        
print()


# all operation in at a time 
print(df.groupby("Course")["Fee"].agg(["sum","max","min","mean","count"]))        


print()
print(df.groupby("Course")["Gender"].count())


print("-"*40)
# for particular course


x = df.groupby("Course").sum()
print(x)

print(x.iloc[1: , : ])

x = df.groupby("Course")["Fee"].sum()['python']
print(x)

print(df[df['Course']=="python"])           # this will give complete information of pyhton 
print(df[df['Course']=="python"].groupby("Course").count())

print(df.groupby("Cours")["Fee"].sum()['pyhton'])