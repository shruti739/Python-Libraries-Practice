'''
piechart : 
    pie() function
    used to check the catogrical data 
    always have to pass numeric data first 

    label =   --> to label all the pie
    explode = [0.0,0.1,0.0] --> to take the pie outside the pie ---> 0.1 for that slice 
    autopct  --> diaplay percentage on slice 
        1 decimal = '%1.1f%%'
        2 decimal = '%1.2f%%'
        0 decimal = '%1.0f%%'
    colors= [] --> to change color each pie diff diff - have to pass in list 
    shadow = True/fales  -> implies to complete pie 
    startangle = (0/90/180,120) ---> changes the start point
    counterclock = True/False  -> to change the direction
    radius = 0.5/1.4/1.8.   --> controls pie size 
    labeldistance = 1.1,            ---> distance of label from the pie 
    rotatelabels= False ,           -----> in the slice direction
    textprops = {'fontsize':10,'color':'black'}             ----> to customize the labels 
    wedgeprops = {'edgecolor' :'black','linewidth':3}    ---> to customize all slices 


    collage , hospital 
'''

import matplotlib.pyplot as plt

act = ['game','food','study','sleep']
rank = [25,70,15,90]
plt.pie(
    rank,               # in pie chart always have to pass numeric data first 
    labels=act,         # to label all pie 
    explode=[0.0,0.0,0.2,0.0],
    autopct= '%1.2f%%',
    colors = ['r','pink','c','brown'],
    shadow=False,
    startangle= 90,
    counterclock=True ,
    radius = 0.7,
    labeldistance = 1.1,
    rotatelabels= False ,
    textprops = {'fontsize':10,'color':'black'},
    wedgeprops = {'edgecolor' :'black','linewidth':3}

)
plt.legend(loc ="lower left")
plt.show()


