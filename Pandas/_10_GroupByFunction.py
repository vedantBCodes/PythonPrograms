import pandas as pd

Info = {
    "Name": ["Rahul", "Amit", "Neha", "Priya", "Kiran", "Sneha"],
    "City": ["Pune", "Mumbai", "Pune", "Mumbai", "Delhi", "Pune"],
    "Marks": [85, 90, 78, 88, 92, 80]
}

data1 = pd.DataFrame(Info);

print(data1);

#  Basic groupby()

group = data1.groupby("City");  # Here group is an object

print(group.groups);

# .get_group() → Get One Group’s Data

print(group.get_group("Pune"));

data1["Gender"] = ['M','F','F','M','M','F'];

print(data1);

