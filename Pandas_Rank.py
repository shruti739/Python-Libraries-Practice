import pandas as pd 

x = [85,75,60,35,90,95]

y=pd.Series(x)
print(y)

# to arrange based on rank - smallest rank will be one  - [85,75,60,35,90,95]               - by default gives o/p on average 
#                                                          4   3  2  1  5  6  - rank 

print(y.rank())     # --> gives the o/p in float
print(y.rank(ascending=False))      

q = y.rank(ascending=False)      
print(q.rank(method='average'))         




