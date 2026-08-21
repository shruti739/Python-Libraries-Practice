import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

d = pd.read_csv("tips.csv")
print(d)

sns.lineplot(
    x = "total_bill",
    y = "tip",
    data = d,
    hue = "sex",
    style = "sex",
    hue_order = ["Female","Male"],       # this will change the order of grouped data 
    markers = ["*","o"],
    dashes = False,
    palette = "muted",
    legend = False
)
plt.show()