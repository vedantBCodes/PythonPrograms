import pandas as pd

Info = {
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Kiran", "Vedant"],
    "Marks": [85, 90, 78, 88, 92, 98],
    "City": ["Pune", "Mumbai", "Delhi", "Nashik", "Nagpur", "Nanded"]
}

data1=pd.DataFrame(Info);

data1.to_csv("data3.csv", index=False);

data2 = pd.read_csv("data3.csv");

print(data2);

# .index → Get Row Index

print(data2.index);

# .columns → Get Column Names

print(data2.columns);

# .describe() → Statistical Summary (Numbers Only)

print(data2.describe());

# .head() → First Rows

print(data2.head(3));  # Default → first 5 rows

# .tail() → Last Rows

print(data2.tail(3));  # Default → Last 5 rows

# Slice First n Rows
n=3;
print(data2[:n]);

# type() → Check Data Type

print(type(data2));

#  .sort_index() → Sort by Index

print (data2.sort_index());

#  .loc → Label Based Selection loc-location

print("\n\n",data2.loc[3]);  # print the data from the 4rd row / 3rd index(i.e record of Priya)
print(data2.loc[3,"Marks"]); # print the marks of Priya
print(data2.loc[:,"Marks"]); # Print the marks of all the students
print(data2.loc[:,["Name","Marks"]]); # Print the name and marks of all the students


print(data2.loc[data2["Marks"] > 85]);

# .iloc → Position Based Selection

print(data2.iloc[1]);  # Select 1st row
print(data2.iloc[1,2]);  # Select data from 1st row and 2nd column
print(data2.iloc[:3]);  # Select rows from 1 to 3

print(data2.iloc[[1,2,3,4]]);














