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

    hach - to fill the bar(inside) - /,+,* etc
        
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
bar chart -
    to compare two set of data 
    bar() types :
        vartaical , horizantal , grouped 
'''

'''
import matplotlib.pyplot as plt
import numpy as np

bowelr_name = ["A","B","C","D","E"]
Runs = [10,5,3,15,8]

plt.bar(
    bowelr_name,
    Runs,
    color = ['pink','brown','red','c','y'],
    width = 0.5,
    edgecolor = 'black',
    label = "Runs",
    hatch = "/"

)
plt.title("Cricket",fontsize = 8,color = 'blue')
plt.xlabel("Bowelr_name",fontsize = 8,color = 'blue')
plt.ylabel("Runs",fontsize = 8,color = 'blue')

plt.legend()
plt.show()
'''







# tow bar will overlap over one another - if done this way 
'''
import matplotlib.pyplot as plt

sub=['python','SQL','Java','Manual']
boys = [50,35,40,60]
girls = [25,10,70,30]

plt.bar(
    sub,
    boys,
    color = 'red',
    width = 0.4
)
plt.bar(
    sub,
    girls,
    color = 'pink',
    width = 0.4
)
plt.show()
'''






# to seperate the bar - for girls and boys 
'''
import matplotlib.pyplot as plt
import numpy as np

sub=['python','SQL','Java','Manual']
boys = [50,35,40,60]
girls = [25,10,70,30]

x = np.arange(len(sub))
print(x)                    # this will diplay the position of subject - [0 1 2 3]  -  adding 0.3 to this for girls so position will change 

# to print the boys and girls bar after have to add the width to every sub position 
# boys data will be of - 0.3 and girls data will be - 0.3+0.3  
# so printing boys at x and for boys adding 0.3 for girls data 

# for boys - [0,1,2,3]
# for girls - [0.3,1.3,2.3.3,3.3]


width = 0.3
y=[i+width for i in x]

print(y)

plt.bar(
    x,
    boys,
    color = 'red',
    width = width
)
plt.bar(
    y,
    girls,
    color = 'pink',
    width = width
)
plt.xticks(x+width/2,sub)         # this is to add name to the x-axis   -   /2 to show sub in middle of boys and girls data 
plt.show()
'''





# to print both data in conbine - grouped bar chart

'''
import matplotlib.pyplot as plt
import numpy as np

sub=['python','SQL','Java','Manual']
boys = [50,35,40,60]
girls = [25,10,70,30]
girls_boys=[75,45,110,90]   # add boys and girls 

width = 0.3
x = np.arange(len(sub))         # for boys 
y=[i+width for i in x]          # for girls 
z=[i+width for i in y]          # for combined data 

plt.bar(
    x,
    boys,
    color = 'red',
    width = width,
    edgecolor = 'black',
    label = "boys"
)
plt.bar(
    y,
    girls,
    color = 'pink',
    width = width,
    edgecolor = 'black',
    label = "girls"
)
plt.bar(
    z,
    girls_boys,
    color = 'brown',
    width = width,
    edgecolor = 'black',
    label = "Girls_boys"
)
plt.xticks(x+width/2,sub) 
plt.title("Student Data",fontsize = 20)
plt.xlabel("Subjects")
plt.ylabel("Number of students")
plt.legend(
    facecolor = 'y',
    framealpha = 0.4,
    loc = 'upper left',
    title = "Data",
    title_fontsize = 7
)
plt.show()
'''