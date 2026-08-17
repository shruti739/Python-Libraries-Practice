'''
Numpy - Numerical operation 
        liner , Vetrized programs - w/o using loop programs  
        data clearing , data transform 
        import numpy as np
        to work on array use numpy

        list - slow , more memory , can't perform all operation , loop operation , inerting multiple element is not possible 
        array - fast , less memory , can perform all the operation , no need of looping , multiple inseration is possible 

        directly can't create array in python have to use build-in function array:
            in numpy inbulit function to create array - can use all sequence data(str , list, tule)
            pass homogeneous data 
            
            new_var = np.array(iterable/sequence)

        bool -> int -> float -> complex -> String 

'''

# to check the version 
'''
import pandas as pd
print(pd.__version__)
'''
'''
import numpy as np
print(np.__version__)
'''

import numpy as np


# regarding type 
'''
x = np.array("Hello")
print(x)
print(type(x))
print(x.ndim)   # 0 - bcos accept list and here no list


y = np.array([1])
print(y.ndim)       # 1


z = np.array([1,2,3])
print(type(z))      #<class 'numpy.ndarray'>


s=[1,2,3]
f=np.array(s)
print(type(f))


d= np.array([10,30,40,50.5])
print(d)
'''

# when we are passing heterogenous data works in  -  bool -> int -> float -> complex -> String

'''
d = np.result_type("bool","int")
print(d)                            # when data is of bool and int  o/p will be in - int 

d = np.result_type("int","float")
print(d)                            # float

d = np.result_type("float","complex")
print(d)                            # complex

d = np.result_type("complex","str") 
print(d)                            # str


# example 
w=np.array([10,True,5.6,3+4j,'hi'])         # o/p will be in str data type - bcos highest in herarchicy
print(w)
'''



# how to create empty array 
'''
d = np.array([])
print(d)
print(d.ndim)
'''

# to create 1d array
'''
y = np.array([23,45,67])
print(y)
print(y.ndim)
'''

# how to create 2d array    -   o/p in matrix formate   -  use nested array 
'''
y = np.array([[10,20,30],[40,50,60]])
print(y)
print(y.ndim)        # ---> 2D array 
print(y.shape) 
'''


# 3D array 
'''
w = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(w)            # ---> 3D


# to caluculate total no of element 
print(w.size)

print(w.shape)      # (1, 3, 3) ---> (3,3) - sixe of matrix 3x3  1 -> outer []
'''


'''
s = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(s)
print(s.shape)
'''


# to reshape  -  multipe should be same (3,4) = 12 , (6,2)=12 then only reshape is possible 
'''
x = s.reshape(3,4)
print(x)
print(x.shape)

x = s.reshape(6,2)
print(x)
print(x.shape)

x = s.reshape(1,12)
print(x)
print(x.shape)
'''

# to covert multi Dimension to ---> single dimension
'''
q = s.reshape(-1)
print(q)
print(q.ndim)
'''
'''
s = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])

w = s.flatten()         # all data rearrang row by row 
print(w)
w = s.flatten(order="C")         # all data rearrang row by row - "C" arrange row by row  - this by default 
print(w)
w = s.flatten(order="F")         # all data rearrang row by row - arranges data in list column by column 
print(w)


k = s.ravel()
print(k)
k = s.ravel(order = "C")
print(k)
k = s.ravel(order = "F")
print(k)
'''



# shallow copy modification wont affect the copy
'''
a = np.array([1,2,3,4,5])
b = a.copy()               
print(a)
print(b)

a[0]=900
print(a)
print(b)

b[0]=500
print(a)
print(b)
'''



# View - Modification done in one var will affect other var 
'''
a = np.array([1,2,3,4,5])
b=a.view()
a[0]=900
print(a)
print(b)

b[0]=500
print(b)
print(a)
'''

# diff b/w flatten and ravel :  flatten = copy , ravel = view
# flatten
'''
a = np.array([[[1,2,3],[4,5,6]]])
b=a.flatten()                       # wont affect other var just like copy
print(a)
print(b)

b[0]=900
print(a)
print(b)
'''


'''
a = np.array([[[1,2,3],[4,5,6]]])
b=a.ravel()                       # will affect other var just like copy
print(a)
print(b)

b[0]=900
print(a)
print(b)
'''