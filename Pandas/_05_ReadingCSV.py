import pandas as pd

# Read a CSV File in Pandas

data = pd.read_csv("data1.csv");

print(data);

# ✅ 1. Read Data from One Column
# Using Column Name
marks = data["Marks"];  # Here Marks is the column name
print(marks);

# ✅ 2. Read a particular record
record_1 = data.iloc[0];  # Here 0 is the index number
print(record_1);

# ✅ 3. Read multiple Columns Using usecols
# Example: Read "Name" and "City"
data1 = pd.read_csv("data1.csv", usecols=["Name", "City"]);
print(data1);

# Give Custom Column Names
data2 = pd.read_csv(
    "data1.csv",
    header=None,
    names=["Name", "Marks", "City"]
)

print(data2);




