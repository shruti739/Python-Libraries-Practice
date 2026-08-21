import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

d = pd.read_csv("tips.csv")
print(d)
'''
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
    legend = False,
    markersize = 5
)
plt.title("Tips_dataset_Lineplot chart")
plt.grid()
plt.show()
'''

'''
sns.lineplot(
    x = "tip",
    y = "total_bill",
    data = d,
    hue = "smoker",
    style = "smoker",
    dashes = False,
    palette = "Blues"
)
plt.title("Tips_dataset_Lineplot chart")
plt.grid()
plt.show()
'''



sns.lineplot(
    x = "tip",
    y = "total_bill",
    data = d,
    hue = "smoker",
    style = "time",
    dashes = False,
    palette = "deep",
    color = ["brown","pink"]
)
plt.title("Tips_dataset_Lineplot chart")
plt.grid()
plt.show()

