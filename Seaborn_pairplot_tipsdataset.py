'''
relation netween two variables
'''

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

d = pd.read_csv("tips.csv")
print(d)

# sns.scatterplot(
#     x = "tip",
#     y = "total_bill",
#     data = d,
#     hue = "sex",
#     style = "sex",
#     markers =["*","<"],
#     s = 100,                 # to change the size of the marker
#     alpha = 0.7
# )
# plt.title("Tips_dataset_Scatterplot chart")
# plt.grid()
# plt.show()

sns.pairplot(d)
plt.show()