# var_name = pd.pivot_table(data,index,values,arrfunc)
#  data - var of data frame 
#  index - for row 
#  value -  the column on which aggfun has to apply
#  aggfunc - what operation we have to perform

import pandas as pd 

emp_name = ["Sachine","Rahul","Ravi","Ravi","Mani"]
product = ["Mobile","Laptop","Remote","Laptop","Mobile"]
sal=[10000,15000,7000,18000,9000]
city = ["Pune","Chandrapur","Mumbai","Pune","Chandrapur"]
rating = [1,2,3,4,5]

data = {"Name":emp_name,"Product":product,"Sales":sal,"City":city,"Rating":rating}

df = pd.DataFrame(data)
print(df)

y =pd.pivot_table(df,index="Name",values="Sales",aggfunc="mean")
print(y)

y =pd.pivot_table(df,index="Name",values="Sales",aggfunc="count")
print(y)

y =pd.pivot_table(df,index="Name",values="Sales",aggfunc="max")
print(y)

y =pd.pivot_table(df,index="Name",values="Sales",aggfunc="min")
print(y)

y =pd.pivot_table(df,index="Name",values="Sales",aggfunc=["min","max","mean","sum","count"])
print(y)

y =pd.pivot_table(df,index="Name",values="Sales",aggfunc="count",margins=True,margins_name="Total")     # for total sum , to change the name - by default 'All'
print(y)

y =pd.pivot_table(df,index="Product",values="Rating",aggfunc="mean")    
print(y)


