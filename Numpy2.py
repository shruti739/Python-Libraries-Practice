import numpy as np 

x = np.array([1,2,3,4,5,6])
print(x)
print()

y = np.repeat(x,3)      # repeats each element 3 times 
print(y)
print()

# arrange() --  new_var = np.arange(start,stop,stepvalue)

s = np.arange(1,10+1,1)
print(s)
print(s)

s = np.arange(1,11,1)
print(s)
print()

s1 = np.arange(1.1,5.1,1)   # works like range 
print(s1)
print()

s1 = np.arange(1.1,5.1,1.1) 
print(s1)
print()

s2 = np.linspace(1,10,3,retstep=True)       # returns equally spaced value , here - 3 value 
print(s2)
print()

# retstep=True tells NumPy to return the step size along with the array.
# linspace -→ values
# retstep=True -→ values + step size
'''
5.5 - 1 = 4.5
10 - 5.5 = 4.5
(
    array([1. , 5.5, 10. ]),
    4.5
)
'''



x=np.array([1,2,3,4,5,8,9,3,5,1,2,10,15,10])
print(x)
print()
y=np.unique(x)
print(y)
print()
y=np.unique(x,return_index=True,return_counts=True)
print(y)
'''
([ 1,  2,  3,  4,  5,  8,  9, 10, 15]),              # unique values
 array([ 0,  1,  2,  3,  4,  5,  6, 11, 12]),      # first indexes
 array([2, 2, 2, 1, 2, 1, 1, 2, 1]))                 # counts
'''
