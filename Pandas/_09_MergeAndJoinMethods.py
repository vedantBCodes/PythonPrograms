import pandas as pd

Info1 = {
    "Name":["Veda","Surjya","Bauna","Pitte","Aamu","Swaraj"],
    "ID":[1,2,3,4,5,6],
    "Marks":[70,80,75,85,90,40]
}

Info2 = {
    "ID":[1,2,3,4,7,8],
    "Degree":["MCA","BCA","BTech","MTech","BA","MBA"],
    "Subject":["Math","English","Marathi","Science","History","Geography"]
}

df1 = pd.DataFrame(Info1);
df2 = pd.DataFrame(Info2);

df3 = pd.merge(df1,df2,on="ID");  # (Inner Join – Default)

print(df3);

# Types of Merge

# (a) Inner Join (Default)

df4= pd.merge(df1,df2,on="ID",how="inner");
print(df4);  # Displays the common records

# (b) Left Join

df5= pd.merge(df1,df2,on="ID",how="left");
print(df5);  # Displays the common records along with the remaining all records of the left Dataframes

# (c) Right Join

df6= pd.merge(df1,df2,on="ID",how="right");
print(df6);  # Displays the common records along with the remaining all records of the right Dataframes

# (d) Outer Join

df7= pd.merge(df1,df2,on="ID",how="outer");
print(df7);  # Displays all the records of the both right and left Dataframes

Info3 = {
    "Name":["Ritesh","Vinod"],
    "ID":[11,12],
    "Marks":[78,89]
}

df8 = pd.DataFrame(Info3);

df9=pd.concat([df1,df8]); # Add some new records by creating new rows

print(df9);



