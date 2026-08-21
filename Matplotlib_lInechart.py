'''
Used for data visualization
to work on matplotlib have to use .pyplot package 

charts : 
    line
    scatter
    barchart
    pie chart
    grid chart
    grouped chart
    Histogram chart

comportants in chart : 
    box - figure (inside which garph is present)
    x,y,z - directions (axis)
    axes - place of the chart 
    color=" "  - to change the line colour 
    linestyle='solid'(by default) , 'dotted', 'dashdot' ,"dashed" , 'None' (no line only axis)       ---> To change the line style 
                    _____                 ......    -.-.-.    ------
        linewidth / lw  -  to change the line size
    marker=  - to highlight the data (* ,^[triangle up],v[triangle down],o,s,+,x,D[dimand])
    ms - Makrer size
    mfc [ marker face colour]  -  to change the marker face colour
    mec [ marker edge colour] -  to change the edge colour of marker
    mew [ marker edge width] 

        
    xlabel , ylabel , zlabel = To tell what data we are showing   ----> these are function can't access in plot()
    title() - outside the plot()
    
    show() - to display the chart

    legend() - to know the info from chart

    grid() - to add the lines in chart
        color
        axis - 'x','y','both'(by default) 
        ls - linestyle
        lw - line width

'''

import matplotlib.pyplot as plt
#      package    module






'''
line chart -
    trend analysis , growth
    plot() - to create line chart
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,11,2)
print(x)
y = x**2
print(y)
z = y**2
print(z)


plt.plot(
    x,
    y,
    color = 'Red',
    linestyle = 'dashed',
    marker = 'o',
    ms = 15,
    mec = 'y',
    mfc = 'c',
    linewidth = 3,
    label = "Trends_growths" ,       # what type to info have to show , but not printing 
    markeredgewidth = 5
)
plt.plot(x,z,color ="c" )

plt.title("Linechart",fontsize = 20,color = 'blue')
plt.xlabel("X axis",fontsize = 20,color = 'brown')
plt.ylabel("Y axis",fontsize = 20,color = 'brown')
plt.legend(loc ="upper right",
           fontsize = 10,
           title = 'Line',
           title_fontsize = 5,
           frameon = True,
           facecolor = "yellow",
           edgecolor = "red",
           shadow = False,
           fancybox = False,
           framealpha = 0.4
        )        # to print the legend     loc - to chnage thhe position of the legend 
plt.grid(axis='both',
         color = 'pink',
         ls="dotted",
         lw = 2
    )
plt.show()


'''
        Legend parameter
 loc 
 fontsize
 title
 title_fontsize
 frameon = True/False -  to show/hide legend box(border) , not inside inforamtion
 facecolor - to change the colour of the box  / background color 
 edgecolour 
 shadow - addes shadow to the box 
 fancybox - true (curve the box in cornner) / false (90 degree corrner)
 farmealpha  - (0 - 1)
'''