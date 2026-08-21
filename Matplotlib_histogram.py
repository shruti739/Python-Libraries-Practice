'''
Histogram : 
    data distribution 
    only numerical data - on the basis of groups - group that data 
    bins= - to make the group of data 
    hist() - accepts only numerical data 
    in bar - comapre data , hist - group data (only numerical)
    main parameters :
        var_name , 
        bins , 
        color
'''


import matplotlib.pyplot as plt

result = [10,12,15,18,21,25,30,35,40,47,50]
plt.hist(
    result,
    bins = 7,
    rwidth = 0.8,               # if not mentioned all bars will merge
    color='skyblue',
    label = 'data',
    #orientation = 'horizontal',              # bar direction/position - by default vertical 
    orientation = 'vertical', 
    align = 'right',                 # this will change the value - if the bar group b/w 10-20 --> mid = 15,left = 10 ,right = 20
    histtype= "bar",                    # this will print the bars in step / bar / stepfilled 
    cumulative = False ,              # is used to show the running/cumulative frequency instead of the frequency of each individual bin. - bar1 = bar1 --> bar2 =bar1+bar2 --> bar3 = bar1+2+3
    edgecolor = "black",
    hatch = "/" ,
    #range = (45,50),              # (min_num,max_num) = From what value to what value should those bins cover? --> range controls the data interval , bins controls how that interval is divided.

)           
plt.title(
    "Histogram",
    fontdict={"fontsize":20,"color":'brown'}
)
plt.xlabel(
    "Value_data",
    fontdict={"fontsize":20,"color":'brown'}
)
plt.ylabel(
    "Y axis data",
    fontdict={"fontsize":20,"color":'brown'}
)
plt.legend()
plt.grid()
plt.show()






# manually bins 
'''
10 ─── 20 ─── 30 ─── 40 ─── 50
  bin1   bin2   bin3   bin4
'''
'''
import matplotlib.pyplot as plt

result = [10,12,15,18,21,25,30,35,40,47,50]
plt.hist(
    result,
    bins = [10,20,30,40],
    rwidth = 0.8
)
plt.title("Histogram")
plt.xlabel("Value_data")
plt.ylabel("Y axis data")
plt.show() 
'''