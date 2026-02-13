import pandas as pd

# CREATING SERIES

# 1. Create Series from a List
marks = [10,20,30,40,50];

data1 = pd.Series(marks);  # Here data1 is the name of the series

print(data1);

# 2. Create Series with Custom Index

data2 = pd.Series(marks, index=["Vedant","Rahul","Surjya","Prithvi","Pitte"]);

print(data2);

#  3. Create Series from Dictionary

data3 = {
    "Ram": 80,
    "Sam": 75,
    "Raj": 90,
    "Tom": 60
}

print(data3);

# Accessing Data from Series

# 1.By Index Number

print(data1[0]);

# 2.By Index Name

print(data2["Rahul"]);

# 3.Multiple Values

print(data2[["Rahul","Surjya"]]);

# Useful Series Properties

# Get Values
print(data1.values);

# Get Index
print(data1.index);

# Get Data Type
print(data1.dtype);

# Size (Total Elements)
print(data1.size);

# Basic Operations on Series
# Mathematical Operations

# Adds 5 to each value
print(data1 + 5);

# Multiply each value by 2
print(data1 * 2);

# Find Max, Min, Average
print(data1.max());
print(data1.min());
print(data1.mean());

# Filtering Data
print(data1[data1 > 80]);    # Show values greater than 80

# Check Missing Values
print(data1.isnull());

# Remove Missing Values
print(data1.dropna());

# Fill Missing Values
print(data1.fillna(70));






