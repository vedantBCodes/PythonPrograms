password="ved@123";

passwordInput=" ";

print("Username : vedant");

passwordLimit=3;
count=0;

while(password!=passwordInput):
    if (count < passwordLimit):
        passwordInput = input("Enter your logIn ID password :");
        count = count + 1;
    else:
        print("You are out of limit");
        break;
else:
    print("Successfully Loged in !");