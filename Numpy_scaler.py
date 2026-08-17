import numpy as np 

'''
x = np.array([11,12,13,14,15])
res = x+10
print(res)

res1 = x-10
print(res1)

res2 = x*10
print(res2)

res3 = x/10
print(res3)

res4 = x//10
print(res4)

res5 = x%10
print(res5)

res6 = x**2
print(res6)
'''




# indexing ---> var[position]
# if not in index ---> IndexError 
'''
x = np.array([11,12,13,14,15])
print(x[3])
print(x[-5])    # using baclword indexing
'''




# Slicing
'''
x = np.array([11,12,13,14,15])
print(x[0:3:1])
print(x[0:3:2])

# backword indexing
print([x[-1:-4:-1]])
'''




# to print dignoal elements in matrix ---> var_name = np.diag(array_name)
'''
x = np.array([[11,12,13],[14,15,16],[17,18,19]])
print(x)
e = np.diag(x)         
print(e)
'''



# to create 3D matrix using single 1D array 
'''
e = np.array([10,20,30])
print(e)
print()

t=np.diag(e)
print(t)
print()

t1=np.eye(3)        # o/p in the place num 1 and in decimal  # 3 why?  =  to get 3*3 matrix 
print(t1)
print()

t2=np.identity(3)
print(t2)
print()
'''





# to get the index value of array  --->   var_name = np.searchsorted(array,element)
'''
x = np.array([100,150,200,250,900,1000])
print(x)
y = np.searchsorted(x,100)              # ----> 0
print(y)
y = np.searchsorted(x,125)              # ----> 1   if element is not present returns the nearest index 
print(y)



# if unsorted data ---> sort the data --> then find the index 
e = np.array([45,13,89,10,90,5])        # --> unsorted data
print(e)
z=np.sort(e)                            # --> sort the data
print(z)
x = np.searchsorted(z,13)               # then find the index value 
print(x)
'''





# to mearge two array 

# 1] using : concatnate  - 1D array
'''
x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
d = np.concatenate((x,y))
print(d)
'''

# 2D array 
'''
a = np.array([[1,2,3,4],[6,7,8,9]])
b = np.array([[11,12,13,14],[16,17,18,19]])
d = np.concatenate((a,b))
print(d)
print()

d = np.concatenate((a,b),axis=0)
print(d)
print()

d = np.concatenate((a,b),axis=1)
print(d)
print()
'''

# 2] using Stack 

# 1D
a = np.array([1,2,3,4])
y = np.array([6,7,8,9])
d = np.stack((a,y))             #.  unlike concatnate where it 1d i/p - 1d o/p   but in stack 1d i/p - o/p 2D array 
print(d)
d = np.hstack((a,y))        # Combines arrays horizontally
print(d) 
d = np.vstack((a,y))        # Combines arrays vertically (one below another).
print(d)
d = np.dstack((a,y))
print(d)
d = np.column_stack((a,y))
print(d)

# 2D
a = np.array([[1,2,3,4],[6,7,8,9]])
b = np.array([[11,12,13,14],[16,17,18,19]])
d = np.stack((a,b))
print(d)
print()
d = np.hstack((a,b))        # Combines arrays horizontally
print(d) 
print()
d = np.vstack((a,b))        # Combines arrays vertically (one below another).
print(d)
print()
d = np.dstack((a,b))        # depth-wise stacking.
print(d)
print()
d = np.column_stack((a,b))  # Combines 1D arrays as columns.
print(d)
print()

d = np.row_stack((a,b))  #  gives o/p but with warning 
print()


'''
                1D arrays          2D arrays
-------------------------------------------------------
stack()         → 2D               → 3D                 - can apply axis
hstack()        → 1D               → adds columns
vstack()        → 2D               → adds rows          - can't apply axis
dstack()        → 3D               → adds depth
column_stack()  → 2D               → adds columns 
'''