"""
we will need to accept a string and we need to check if the string contains any URL in it.
If the URL is present in the string, we will say URL’s been found or not and print the respective URL present in the string.


Input : string = 'My Profile:
https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
in the portal of https://www.geeksforgeeks.org/'

Output : URLs :  ['https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles',
'https://www.geeksforgeeks.org/']

Input : string = 'I am a blogger at https://geeksforgeeks.org'
Output : URL :  ['https://geeksforgeeks.org']

"""

def checkForURL(str1):
    stringItems=str1.split(" ");
    urlList=[];   #Empty list
    check=False;
    for items in stringItems:
        if(items.startswith("https:")):
            urlList.append(items);
            check=True;
    if(check==True):
        print(f"The URL found in a given string are {urlList}");
    else:
        print("The URL is not found in a given string");

string='My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'

checkForURL(string);