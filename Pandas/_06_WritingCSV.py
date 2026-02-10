import pandas as pd

# Create Data and Convert to CSV

Info = {
    "Name": ["Rahul", "Amit", "Neha"],
    "Marks": [85, 90, 78],
    "City": ["Pune", "Mumbai", "Delhi"]
}

data1 = pd.DataFrame(Info);

data1.to_csv("data2.csv");

# Custom Header Names While Saving
# Method 1: Rename Columns First

data1.columns = ["S_Name", "S_Marks", "S_City"];

# Then save:
data1.to_csv("data2.csv", index=False);

print(data1);

# Method 2: Change Header While Saving
data1.to_csv(
    "data2.csv",
    index=False,
    header=["Student_Name", "Score", "Location"]
)

data1 = pd.read_csv("data2.csv");
print(data1);

# Append Data to Existing CSV (Add More Rows)

data1.to_csv(
    "data2.csv",
    mode="a",
    index=False,
    header=False
)



