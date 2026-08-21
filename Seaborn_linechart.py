'''
Seaborn :
    import the package - import seaborn as sns 
    matplot is the foundation for seaborn 
    sns.show() = attribute error , do not have such function 
    have to use = plt.show()
    interactive charts , 
    always have to use 2D data (dataframe) --> import pandas as pd
    no need to assign x y axis manually - assigned while assigning the data 

'''
'''
line chart :
    lineplot() --> seaborn , plot() --> matplotlib 
    sns.lineplot(
        x = value,
        y = value,
        data = dataframe_name       # if not passed -> valueerror 
    )
    hue - to group the chart on the basis of any value in dataframe 
    legend gets created automatically
'''

#-------- Normal chart ----------#
'''
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

x=[10,20,30,40,50]
y=[15,25,35,45,55]
plt.plot(x,y)
plt.xlabel('X')
plt.xlabel('Y')
plt.show()
'''


#---------Seaborn line chart---------#
'''
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

x=[10,20,30,40,50]
y=[15,25,35,45,55]
sns.lineplot(x=x,y=y)

#sns.show()              # AttributeError: module 'seaborn' has no attribute 'show'
'''




# using data frame 

import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

name=['A','B','C','D']
marks = [35,67,89,90]
gender = ["M","F","M","F"]

d = {'NAME':name,'MARKS':marks,'Gender':gender}

df=pd.DataFrame(d)
print(df)

sns.lineplot(
    x = "NAME",         # data on x-axis 
    y = "MARKS",        # data on y-axis
    data = df,          # datafame from where we are accessing x and y axis data    
    hue = "Gender",     # to groups the data on the basis of value , here gender 
    #style = "Gender",   # change the line style diff gender
    markers = "o" ,
    markersize = 10,
    linewidth = 2,
    linestyle = "dotted",       # linestyle and style won't work together 
    legend = False 

)
plt.show()