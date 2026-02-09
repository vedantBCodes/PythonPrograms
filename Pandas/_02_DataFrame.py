import pandas as pd

# Creating DataFrame

# 1.Create DataFrame from List

Info1 = [["Vedant",70,85],
         ["Rahul",90,95],
         ["Surjya",80,90],
         ["Swaraj",50,60],
         ["Prithvi",90,95],
         ["Pitte",85,98]
         ];

data1=pd.DataFrame(Info1);

print(data1);

data2=pd.DataFrame(Info1,columns=["Name","Marks1","Marks2"]);

print(data2);

# 2.Create DataFrame from List of Tuples

Info2 = [
    ("Ram", 80, 20),
    ("Sam", 75, 19),
    ("Raj", 90, 21)
]
data3 = pd.DataFrame(Info2, columns=["Name", "Marks", "Age"]);

print(data3);

# 3.Create DataFrame from Dictionary


Info3 = {"Vedant":[70,85],
         "Rahul":[90,95],
         "Surjya":[80,90]
         };

data4 = pd.DataFrame(Info3);

print(data4);

# Create DataFrame from Dictionary of Series

name = pd.Series(["Ram", "Sam", "Raj"])
marks = pd.Series([80, 75, 90])
age = pd.Series([20, 19, 21])
Info4 = {
    "Name": name,
    "Marks": marks,
    "Age": age
}

data5 = pd.DataFrame(Info4);
print("Data5 :" ,data5);

# Accessing Data in DataFrame
# 🔹 View First Rows
print(data1.head());  # Display first 5 records

# 🔹 View Last Rows
print(data1.tail());  # Display last 5 records

# 🔹 Get Column
print(data2["Marks1"]);

# 🔹 Get Multiple Columns
print(data2[["Name", "Marks1"]]);

# 🔹 Get Row (By Index)
print(data1.loc[0]);


# 📌 Basic Operations on DataFrame

# 🟢 Find Average, Max, Min
print(data2["Marks1"].mean());
print(data2["Marks1"].max());
print(data2["Marks1"].min());

# 🟢 Filter Data
print(data2[data2["Marks1"] > 80]);

# 🟢 Add New Column
data2["Result"] = ["Pass", "Fail", "Pass","Fail","Pass","Pass"]

# 🟢 Delete Column
data2.drop("Marks2", axis=1, inplace=True);







