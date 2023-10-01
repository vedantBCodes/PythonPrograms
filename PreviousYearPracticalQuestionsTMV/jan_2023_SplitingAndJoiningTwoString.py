#Joining two strings

fname=input("Enter your first name : ");
sirname=input("Enter your sirname :");

fullName= fname + " " + sirname ;

print(f"Your full name is : {fullName}");

#Spliting two strings

fullName=input("Enter your full name (first name and sirname seperated by space) :");

fname,sirname=fullName.split();

print(f"Your name is {fname}");
print(f"Your sirname is {sirname}");