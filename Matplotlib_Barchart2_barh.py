'''
Used for data visualization
to work on matplotlib have to use .pyplot package 

charts : 
    line
    scatter
    barchart
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

import matplotlib.pyplot as plt
#      package    module




'''
barh chart -
    to compare two set of data 
    bar():
        vartaical , horizantal , grouped 
    width not allowed 

'''


import matplotlib.pyplot as plt
import numpy as np

bowelr_name = ["A","B","C","D","E"]
Runs = [10,5,3,15,8]

plt.barh(
    bowelr_name,
    Runs,
    color = ['pink','brown','red','c','y'],
    edgecolor = 'black',
    label = "Runs",

)
plt.title("Cricket",fontsize = 8,color = 'blue')
plt.xlabel("Bowelr_name",fontsize = 8,color = 'blue')
plt.ylabel("Runs",fontsize = 8,color = 'blue')

plt.legend()
plt.show()