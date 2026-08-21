'''
Subplot():
    multiple chart in single chart
    subplot() 
    works on the basis of : RCI - R = number of rows , c = no. of column , I = Index positionof chart (strts with - 1)
^           ^
|           |
|           |                                      R C I
|----->     |----->         1 row - 2 column   A -(1,2,1), B-(1,2,2)        # ---> left to right indexing
 A           B
'''



'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,20,25,30]
z = [15,20,25,30,35]
z1 = [20,25,30,35,40]

plt.suptitle("SubPlot chart")          
plt.figure(figsize=(10,8))         # (width,hight)
plt.subplot(3,2,1)
plt.plot(
    x,
    y,
    linestyle = "dotted",
    color = 'black'
)
plt.title("Line chart")
plt.subplot(3,2,2)
plt.scatter(
    y,
    z,
    color = "c",
    marker='*',
    s = 200
)
plt.title("Scatter chart")
plt.subplot(3,2,3)
plt.hist(
    z,
    color = 'r'
)
plt.subplot(3,2,4)
plt.pie(
    z1,
    labels=['A','B','C','D','E']
)
plt.subplot(3,2,5)
plt.barh(
    x,
    z1,
    color = 'orange'
)
plt.legend(loc="upper right")
plt.show()


'''
