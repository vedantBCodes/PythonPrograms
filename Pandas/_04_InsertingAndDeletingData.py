import pandas as pd

# Insert a New Column (Manually Add Data)

Info = {
    "Name": ["Surjya", "Vedant", "Pitte"],
    "Marks": [85, 90, 78],
    "City": ["Pune", "Mumbai", "Delhi"]
}

data = pd.DataFrame(Info);

print(data);

# Method 1: Using [] (Most Common)

data["Age"] = [20,32,12];

print(data);

# Method 2: Using insert() (Choose Position)

data.insert(1,"RollNo",[1,2,3]);

print(data);

#  Create New Column by Copying Existing Column

# Method 1: Direct Copy (Most Used)
data["Marks_Copy"] = data["Marks"];

# Method 2: With Calculation (Bonus)
# Example: Add 5 bonus marks
data["Final_Marks"] = data["Marks"] + 5;

print(data);

# Delete / Remove a Column

# Method 1: Using drop() (Recommended)

data.drop("City", axis=1, inplace=True);

# Method 2: Using del Keyword

del data["Age"];

print(data);










