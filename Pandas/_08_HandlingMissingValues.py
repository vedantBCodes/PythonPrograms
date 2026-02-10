import pandas as pd
import numpy as np

# 1.Create Sample Data with Missing Values

Info={
    "Name":["Vedant",np.nan,"Surjya","Pitte","Prithvi"],
    "Age":[20,np.nan,27,53,np.nan],
    "City":[np.nan,"Mukhed","Latur",np.nan,"Pune"],
    "RollNo":[5,10,15,20,25]
}

data1=pd.DataFrame(Info);

data1.to_csv("data4.csv");

# print(data1);

# 2.Check Missing Values First

# Before handling them:
# Check where values are missing
print(data1.isna());  #It will return the whole data with True of there is a missing value and False if there is something other than NaN

# 3.Count missing values
print(data1.isna().sum());  #It will show the no. of missing values per column with column name

# 4.dropna() → Remove Missing Data   --> dropna() deletes rows/columns that contain NaN.

# 4.1 Remove Rows with Any NaN (Default)
df1 =data1.dropna();
print(df1);

# Removes any row that has at least one NaN.
# 4.2 Remove Columns with NaN
df2 = data1.dropna(axis=1);
print(df2);

# axis=1 → columns
# 4.3 Remove Row Only If ALL Values Are NaN
df3 = data1.dropna(how="all");
print(df3);

# Removes row only if all values are missing.
# 4.4 Keep Rows with Minimum Data
# Example: Keep rows with at least 2 non-NaN values:
df4 = data1.dropna(thresh=2);
print(df4);

# 4.5 Modify Original Data (inplace)
df5 = data1.dropna(inplace=True);
print(df5);

# ⚠️ Original data is changed permanently.

# ✅ 5.1 Fill with a Fixed Value
# Fill all NaN with 0
df6 = data1.fillna(0);
print("After FillNA");
print(df6);

# Fill with "Unknown"
df7 = data1.fillna("Unknown");

print(df7);

# replace() → Convert Wrong Values to NaN

data1.replace(np.nan,3000,inplace=True);

print("After Replace\n" ,data1);

data1.replace(3000,"Unknown",inplace=True);

print("After Replace\n" ,data1);

