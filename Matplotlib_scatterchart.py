'''
scatter chart :
    relation betweent two variables 
    data present in dotted 
    always have to use numerical data
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,1)
y = x**2
plt.scatter(
        x,
        y,
        marker = "*",
        s =500,
        color = ['r','black','b','pink','brown'],
        alpha= 0.7,
        edgecolor = 'black',
        linewidth = 1,
        label = "Squar"

    )
plt.title("Scatter Chart",fontsize = 20)
plt.xlabel("x-axis",fontsize = 20)
plt.ylabel("y-axis",fontsize = 20)
plt.grid()
plt.legend(facecolor = 'red',framealpha = 0.4)
plt.colormaps()
plt.colorbar()
plt.show()