import pandas as pd

# Arithmetic & Relational Operations in Pandas

Info = {
    "A": [10, 20, 30, 40],
    "B": [5, 25, 15, 35]
}

data = pd.DataFrame(Info);

print(data);

# 1. Arithmetic Operations ( Math Operations )

data["Add"] = data["A"] + data["B"];

data["Sub"] = data["A"] - data["B"];

data["Mul"] = data["A"] * data["B"];

data["Div"] = data["A"] / data["B"];

print(data);

# 2. Relational Operators (Comparison Operators)

# Check: Is A > B ?
data["A_greater_B"] = data["A"] > data["B"];

# Check: Is A == B ?
data["A_equal_B"] = data["A"] == data["B"];

# Check: Is A < B ?
data["A_less_B"] = data["A"] < data["B"];

print(data);

# 3. Combine Conditions (Bonus – Very Useful 🔥)

# You can also use logical operators:
# Example: A > B AND A > 25

data["A_gt_B_and_25"] = (data["A"] > data["B"]) & (data["A"] > 25)

print(data);



