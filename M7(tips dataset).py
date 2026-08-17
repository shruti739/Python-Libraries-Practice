import pandas as pd 


# Dataset Understanding Questions
#---------------------------------------------------

# 1. Import the Dataset  
df = pd.read_csv("tips.csv")
print(df)

# 2. Display Last 5 Rows
print("Last 5 Rows : ")
print(df.tail())

# 3. Find Dataset Size
print("Sixe of dataset is :")
print(df.shape)

# 4. Display Column Names
print("Column names are : ")
print(df.columns)

# 5. Check Data Types
print("Data types of each column : ")
print(df.dtypes)

# 6. Display Dataset Information
print("Dataset information : ")
print(df.describe())

# 7. Generate Statistical Summary
print("Statistical Summary : ")
print(df.describe(include="number"))


# 8. Display 10 Random Records
print("Random records : ")
print(df.sample(10))



# How to Selecting Data from dataset
# ----------------------------------------------------


# 9. Select total_bill
print("Total Bill : ")
print(df[["total_bill"]])


# 10. Select Multiple Columns
print("Total Bill : ")
print(df.loc[[0,1]])


# 11. Select First 10 Rows

# 12. Select Specific Rows and Columns

# 13. Select Using loc
 


# How to Filtering The Data from dataset
# -------------------------------------------------------

# 14. Bills Greater Than 30

# 15. Tips Greater Than 5

# 16. Female Customers(Display all records)


# 17.Display all smoker records

# 18. Display all records of Saturday

# 19.Large Groups Display customer (size>=4)

# 20.Display the data day will be Saturday and time will be dinner

# 21.Display all unique values from the day column.

# 22.Find the number of unique days.

# 23.Find how many records belong to each day

# 24.Count Smokers and Non-Smokers

# 25.Find the highest total_bill.

# 26.Find the smallest tip.
























































