import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,20,25,30]
z = [3,4,5,6,7]

plt.plot(x,y,color = 'r',marker = "*")
plt.plot(x,z,color = 'c')
plt.fill_between(x,y,color = 'r')
plt.fill_between(x,z,color = 'c')

plt.show()