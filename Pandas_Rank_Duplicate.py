import pandas as pd 

# by default decending - ranking 

# in case of duplicate numbers  
'''
1  -  sort
2  -  rank the elements 
3  - 
'''
x = [85,75,60,90,90,95]
#  [60,75,85,90,90,95]
#   6  5  4  3  2  1   -->  find avg(mean) of duplicate element i.e.  90 - 2.5 for both 


y=pd.Series(x)
print(y)

q = y.rank(ascending=False)      
print(q.rank(method='average'))         


# among duplicate max rank will among all will be the rank of rest of duplicates  and same with minimum 
print(q.rank(method='max'))
print(q.rank(method='min'))
print(q.rank(method='first'))        # ranking in continous dispit of duplicate element 
print(q.rank(method='dense'))       # duplicate elements will have same rank with no gap 










print('-'*40)

s=[99,95,85,75,75,65]

d=pd.Series(s)
print(d)
print()

z = d.rank(ascending=False)
print(z.rank(method='average'))   
print()  
print(z.rank(method='max'))     
print()
print(z.rank(method='min'))
print()
print(z.rank(method='first'))      
print()
print(z.rank(method='dense'))       # 1,2,3,4,4,5 - before - 1,2,3,4.5,4.5,6






