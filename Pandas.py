'''
Series - this helps to create the series of elements
'''



'''
import pandas as pd 
data = [ 34,67,11,90,1,105]
x=pd.Series(data)
print(x)
print()
print(x.sort_values())        # by default - A--->D
print()
print(x.sort_values(ascending = True))     # A--->D
print()
print(x.sort_values(ascending = False))   # D-->A  

# working on values , to work on index

'''

'''
import pandas as pd
data = [ 34,67,11,90,1,105]
x=pd.Series(data)
print(x)
print()
print(x.sort_index())        
print()
'''

'''
import pandas as pd
t = [10,20,30,35,36]
d= pd.Series(t)
print(d)
print()
print(d.where(d>30))
'''



'''
import pandas as pd 
t=[45,33,20,10,43,45]
d=pd.Series(t)        # this creats the series of the given data 
print(d)
print(d.where(d<45))
'''


'''
import pandas as pd
t=[45,33,20,10,43,45]
d=pd.Series(t)        
print(d)
print(d.where(d<45))
print(d.mask(d<45,"Value"))       # show NaN or content in " " if condition satisfy opp to where 
'''

'''
import pandas as pd
w=[100,None,200,None,400,800]
s=pd.Series(w)
print(s)
print(s.isnull())     # True -- Value not present (None) , False --  Element present
print()
print(s.notnull()) 
print()
print(s[s.isnull()])   
print()
print(s[s.notnull()])         # to get the values and not the Boolean values --> Pure information 
'''



'''
name = ["A","B","C","D","E"]
Eid = ["A12","B45","C89","D55","E99"]
sal = [1000,2000,3000,4000,5000]
yoe = [5,7,9,10,4]

details = {"NAME":name,"EID":Eid,"SAL":sal,"YOE":yoe}      #have to pass the data in dict formate {"Col_name" : list_name}.   col_name should starts with Csplatter

                            # syntax   new_var = pd.DataFrame(dict_name)       

df = pd.DataFrame(details)
print(df)
'''


'''
name = ["A","B","C","D","E"]
Eid = ["A12","B45","C89","D55","E99"]
sal = [1000,2000,3000,4000,5000]
yoe = [5,7,9,10,4]

details = {"NAME":name,"EID":Eid,"SAL":sal,"YOE":yoe}      
df = pd.DataFrame(details)
print(df)
print()
print(df.ndim)
print()
print(df.shape)
print()
print(df.index)
print()
print(df.columns)
print()
print(df.dtypes)
print()
print(type(df))
print()
df.info
print()
print(df.describe())          # only works with numerical comlun --> does the calculation   ----> by default
print()
print(df.describe(include="number"))    # manually
print()
print(df.describe(include="object"))    # works with character column     -----> freq shows the count of the repetation on the first element    
print()
print(df.describe(include="all"))       # works with both

'''



import pandas as pd
'''
name = ["A","B","C","D","E"]
Eid = ["A12","B45","C89","D55","E99"]
sal = [1000,2000,3000,4000,5000]
yoe = [5,7,9,10,4]

details = {"NAME":name,"EID":Eid,"SAL":sal,"YOE":yoe}      
df = pd.DataFrame(details)

print(df)
print()
print(df.iterrows())            # w/o typcasting - gives memory address 
print()
for i in df.iterrows():           # shows the seperate seperate information -----> givr o/p as memory address so typecasting or looping  
  print(i)
'''


'''
name = ["A","B","C","D","E"]
Eid = ["A12","B45","C89","D55","E99"]
sal = [1000,2000,3000,4000,5000]
yoe = [5,7,9,10,4]

details = {"NAME":name,"EID":Eid,"SAL":sal,"YOE":yoe}      
df = pd.DataFrame(details)

print(df)
print()
print(df.head())        # display first 5 elements ---> by default 
print()
print(df.head(2))       # display first 2 elements 
print()
print(df.tail())        # display last 5 elements ---> by default  
print()
print(df.tail(2))       # display last 2 elements
print()
'''




'''
name = ["A","B","C","D","E"]
Eid = ["A12","B45","C89","D55","E99"]
sal = [1000,2000,3000,4000,5000]
yoe = [5,7,9,10,4]

details = {"NAME":name,"EID":Eid,"SAL":sal,"YOE":yoe}      
df = pd.DataFrame(details)

print(df)
print()
print(df.sample(2))       #randomly 
'''





'''
name = ["A","B","C","D","E"]
Eid = ["A12","B45","C89","D55","E99"]
sal = [1000,2000,3000,4000,5000]
yoe = [5,7,9,10,4]

details = {"NAME":name,"EID":Eid,"SAL":sal,"YOE":yoe}      
df = pd.DataFrame(details)

print(df)
print()
print(df["NAME"])   # to print the single column --- > syntsx. -  var_name["col_name"]
'''




'''
name = ["A","B","C","D","E"]
Eid = ["A12","B45","C89","D55","E99"]
sal = [1000,2000,3000,4000,5000]
yoe = [5,7,9,10,4]

details = {"NAME":name,"EID":Eid,"SAL":sal,"YOE":yoe}      
df = pd.DataFrame(details)

print(df)
print()
print(df["NAME"])   # to print the singlr column --- > syntsx. -  var_name["col_name"]

# to print the multipe column ---> have to use nested list
print(df[["NAME","EID","YOE"]])

'''



'''
import pandas as pd

Name = ["Shruti","Ram","Sham","Rani","Sita"]
age = [21,23,25,21,25]
sub = ["Math","Science","English","SS","M3"]
sub2 = ["Pyhton","PowerBI","Tabluae","Excel","Web"]
total_marks = [300,400,500,600,700]

details = {"Name":Name,"Age":age,"Sub1":sub,"Sub2":sub2,"Total":total_marks}
df = pd.DataFrame(details)
print(df)
print()
print(df.shape)     # gives no of col and rows
print()
print(df.size)
print()
print(df.index)       # range of the rows(index) --->  RangeIndex(start=0, stop=5, step=1)
print()
print(df.axes)        # range of the rows(index) and column name also  ---->   [RangeIndex(start=0, stop=5, step=1), Index(['Name', 'Age', 'Sub1', 'Sub2', 'Total'], dtype='object')]
print()
print(df.columns)
print()
print(df.dtypes)     # data type of each column with name 
print()
print(df.values)     # display all element in nested list 
print()
print(df.ndim)
print()
print(df.empty)
print()
print(df.T)       # Transpose - row to column , column to row
print()
print(df.sample)
'''







# loc [ ] property ----> end index is included - accepts number and column 
'''
import pandas as pd

Name = ["Shruti","Ram","Sham","Rani","Sita"]
age = [21,23,25,21,25]
sub = ["Math","Science","English","SS","M3"]
sub2 = ["Pyhton","PowerBI","Tabluae","Excel","Web"]
total_marks = [300,400,500,600,700]

details = {"Name":Name,"Age":age,"Sub1":sub,"Sub2":sub2,"Total":total_marks}
df = pd.DataFrame(details)
print(df)
print()




# 1] Single row selection ---> df.loc[row_number]
#       gives the complete info about that row


print(df.loc[0])         
print()
print(df.loc[[0,1]])          # to print the multiple rows ----> var_name.loc[[row1,row2]]


# 2] Single row with selected column  ---> df.loc[row_number , ["column_name"]]
#       gives the data of that row and selected column


print(df.loc[2,["Name"]])  
print()  
print(df.loc[3,["Total"]])
print()



# 3] Row range selection  ---> df.loc[start:end_num:step_value] ----> end_num is included ---> step value by default 1
#       gives the data of that row and selected column

print(df.loc[0:2:1])
print()
print(df.loc[::2])
print()


# 4] row range with selected column  ---> df.loc[start:stop:step_value , ["column_name"]
#       gives the data of that row and selected column

print(df.loc[3:5:1],["Name"])
print()




# 5] Row range with multiple column  ---> df.loc[start:stop:step_value , ["column_name1","column_name2"]]
#       gives the data of that row and selected column


print(df.loc[2:5:1,["Name","Age"]])
print()



# 6] column range selection  ---> df.loc[start : stop:step ,"column1":column_last"]
#       prints the column range b/w columns 
 
print(df.loc[0:4:1,"Name":"Sub2"])
print()
'''








# iloc [ ] property ---> end index is excluded. ---->  for column have to mention column number (occurance) ---> only accepts numbers
'''
import pandas as pd

Name = ["Shruti","Ram","Sham","Rani","Sita"]
age = [21,23,25,21,25]
sub = ["Math","Science","English","SS","M3"]
sub2 = ["Pyhton","PowerBI","Tabluae","Excel","Web"]
total_marks = [300,400,500,600,700]

details = {"Name":Name,"Age":age,"Sub1":sub,"Sub2":sub2,"Total":total_marks}
df = pd.DataFrame(details)
print(df)
print()


        # 1] Single row and column ---> df.iloc[row_num,column_num]
        #       gives the data of that row and selected column

print(df.iloc[0,0])       
print()   
print(df.iloc[0,[0]])     # give the column name also
print()
print(df.iloc[1,2])
print()


        # 2] row range and column range ---> df.iloc[row_start : row_stop , col_start:col_stop]
        #       print the data in that range

print(df.iloc[0:2,0:3])           # -----> this will exclude 2nd row (included row - 0,1) and 3rd column (included column - 0,1,2)
print()


   
        # 3] Row range with Single column ---> df.iloc[row_start : row_end ,column_num]
        
print(df.iloc[0:3,0])
print()



        # 4] Multiple selected rows ---> df.iloc[[row1,row2]]

print(df.iloc[1,2])
print()

'''



'''
import pandas as pd

Name = ["Shruti",None,"Sham",None,"Sita"]
age = [21,23,None,21,25]
sub = ["Math",None,"English",None,"M3"]
sub2 = ["Pyhton",None,"Tabluae","Excel","Web"]
total_marks = [None,400,500,600,700]

details = {"Name":Name,"Age":age,"Sub1":sub,"Sub2":sub2,"Total":total_marks}
df = pd.DataFrame(details)
print(df)
print()

print(df.dropna())        # delets the complete row even if single element is not present 
print()

print(df.fillna("*"))     # replays the none value with "*"
print()

print(df.ffill())          # this is forword fill this will replace None with the above value of that column
print()

print(df.bfill())          # this is forword fill this will replace None with the below value of that column
print()
'''




# to create new column in exixting column ---> var["col_name"]=default value /


'''
import pandas as pd

Name = ["Shruti","Ram","Sham","Rani","Sita"]
sal = [21000,23000,25000,21000,25000]

details = {"Name":Name,"Salary":sal}
df = pd.DataFrame(details)
print(df)
print()


df["Total"] = df["Salary"]+100
print(df)


print(df.assign(Total1 = [1,2,3,4,5],Total2 = ["a","d","f","t","u"]))       # adding multiple column at last using inbuild method - assign 



        # shifts the column and insert new column at that position

df.insert(1,"Age",[12,43,21,34,54])
print(df)

'''




'''
import pandas as pd

date_time=["2026-08-06 1:58:30",
           "2026-08-07 2:01:45",
           "2025-05-25 3:30:30"]

details={"DATE_TIME":date_time}
x=pd.DataFrame(details)
print(x)
print()
x["DATE_TIME"]=pd.to_datetime(x["DATE_TIME"])
print(x)
print()
x["YEAR"]=x["DATE_TIME"].dt.year
print(x)
print()
x["MONTH"]=x["DATE_TIME"].dt.month
print(x)
print()
x["DAY"]=x["DATE_TIME"].dt.day
print(x)
print()
x["DAYNAME"]=x["DATE_TIME"].dt.day_name
print(x)
print()
x["HOUR"]=x["DATE_TIME"].dt.hour
x["Second"]=x["DATE_TIME"].dt.second
x["MINUTE"]=x["DATE_TIME"].dt.minute
x["weekday"]=x["DATE_TIME"].dt.weekday
x["Month_Name"]=x["DATE_TIME"].dt.month_name()
print(x)
'''




# ----- Numerical Operations ------#
'''
import pandas as pd

Emp_Name = ["Rohit","Rahual","Ravi","Ram","Rock"]
Emp_id = ["R1","R12","R13","R14","R15"]
Comp_name = ["Ty","IBM","M2p","Amozon","Wipro"]
Emp_sal = [10000,30000,20000,50000,40000]

Details = {"Name":Emp_Name,"ID":Emp_id,"Company":Comp_name,"Salary":Emp_sal}

df = pd.DataFrame(Details)
print(df)

# to perform numerical operations --  sum, mean, median, max, min, mode, count, Valuecount, agg
print()
print("Total Salary : ",df["Salary"].sum())
print()
print("Mean of Salary : ",df["Salary"].mean())
print()
print("Median of Salary : ",df["Salary"].median())               # if the data is not sorted - first internally it will sort the data then median 
print()
print("Mode of repeated : ",df["Salary"].mode())                 # returns the repeted elements 
print()
print("Count of element : ",df["Salary"].count())                 # this will count the no of elements 
print()
print("Count of each element : ",df["Salary"].value_counts())                 # A --> D (count)
print()
print("Count of each element : ",df["Salary"].agg(["sum","mean","median","max","count","min"]))            # this combines all the operation , wont works with mode   
print()


#  to delete the column 

print(df.drop("Salary",axis=1))                  # aixs 1 --> column , axis 2 --> row (by default)
print()
print(df.drop(["Name","ID"],axis=1))          # to delete multiple column at a time 
print()

print(df.drop([1]))           # to delete single row
print()
print(df.drop([1,2]))         # to delete multiple row 
print()

print(df)         # deleting won't affect the original data/table 


# to rename / change column name  -  var_name.rename(coloumns = ({"old_name":"new_name"}))
print()
print(df.rename(columns={"Name":"Ename"}))
print()
print(df.rename(columns={"Name":"Ename","ID":"EID","Company":"Cname"}))            # to change multiple name 

print(df)        # this also won't affect the original data/table 


# to rename / change index name  -  var_name.rename(index = ({"old_index":"new_index"}))
print()
print(df.rename(index= {0:190,1:"hello",2:45}))


# to change the original data. --  inplace = True/False 

print(df.rename(index= {0:190,1:"hello",2:45},inplace=True))
print(df)               # original data is affected 



# to replace particular element
print()
print(df.replace(20000,11000000,inplace=True))
print()
print(df.replace({"Rohit":"Sham","R1":"R11"}))       # to replace the multiple data at a time  
print()
print(df)



# isnull() and notnull()
print()
print(df["Salary"].isnull())
print(df["Salary"].notnull())

print(df.isnull())                  # ---> for complete data 
print(df[df.isnull()])              # ---> even if the data in single column is not presentn print complete row as NaN


# isna() and notna().  ---->  isna()=isnull()    and    notna() = notnull()

print(df.isna())        
print()
print(df.notna())
'''








'''
import pandas as pd

Emp_Name = ["Rohit","Rahual","Ravi","Ram","Rock"]
Emp_id = ["R1","R12","R13","R14","R15"]
Comp_name = ["Ty","IBM","M2p","Amozon","Wipro"]
Emp_sal = [10000,30000,20000,50000,40000]

Details = {"Name":Emp_Name,"ID":Emp_id,"Company":Comp_name,"Salary":Emp_sal}

df = pd.DataFrame(Details)
print(df)




#-------To arrange the data in accending to decending and vise varsa-------#
print()
print(df["Salary"].sort_values())



# value_counts(). ---> df["column"].value_counts()
print()
print(df["Salary"].value_counts())



# unique()  --> df["column"].unique()
print()
print(df["Salary"].unique())



# nunique()  --> df["column"].nunique()
print()
print(df["Salary"].nunique())
'''





'''
import pandas as pd


df = pd.DataFrame({"ID":[10,20,30,40],"Salary":[1000,2000,3000,4000]})

print(df)  



# to change the data type

print(df["ID"].astype(float))

print(df.astype({"ID":complex , "Salary":bool}))            # to change datatype of multiple column 
'''



import pandas as pd 



