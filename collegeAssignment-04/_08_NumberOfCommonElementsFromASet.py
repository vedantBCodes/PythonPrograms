#Number of common items in two sets

set1={1,2,3,4,5};
set2={4,5,6,7,8};

#Method -1    (Using Intersection() Method)

set3=set1.intersection(set2);
len1=len(set3);

print(f"Number of common elements in a given sets are : {len1}");

#Method -2    (Using & operator)

set4=(set1 & set2);

len2=len(set4);

print(f"Number of common elements in a given sets are : {len2}");