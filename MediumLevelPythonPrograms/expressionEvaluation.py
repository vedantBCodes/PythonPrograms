exp="2+4*5-2";

                         #   INCOMPLETE PROGRAM


print(len(exp));
while(len(exp)>2):
    if('*' in exp):
        index=exp.index('*');
        for i in range(index-1,0,-1):
            if(exp[i]=='+' or exp[i]=='-' or exp[i]=='*' or exp[i]=='/'):
                a=i;
        sIndex=exp[a+1];
        for i in range(index+1,len(exp)):
            if(exp[i]=='+' or exp[i]=='-' or exp[i]=='*' or exp[i]=='/'):
                b=i;
        eIndex=exp[b];
        x=exp[a+1:index];
        y=exp[index+1:b];
        ans=int(x) * int(y);
        exp1 = exp[sIndex:eIndex];
        exp=exp.replace(exp1,str(ans));
        print(exp);
        print(len(exp));
    elif('+' in exp):
        index = exp.index('+');
        for i in range(index - 1, 0, -1):
            if (exp[i] == '+' or exp[i] == '-' or exp[i] == '*' or exp[i] == '/'):
                a = i;
        sIndex = exp[a + 1];
        for i in range(index + 1, len(exp)):
            if (exp[i] == '+' or exp[i] == '-' or exp[i] == '*' or exp[i] == '/'):
                b = i;
        eIndex = exp[b];
        x = exp[a + 1:index];
        y = exp[index + 1:b];
        ans = int(x) + int(y);
        exp1 = exp[sIndex:eIndex];
        exp = exp.replace(exp1, str(ans));
        print(exp);
        print(len(exp));
    elif ('-' in exp):
        index = exp.index('-');
        for i in range(index - 1, 0, -1):
            if (exp[i] == '+' or exp[i] == '-' or exp[i] == '*' or exp[i] == '/'):
                a = i;
        sIndex = exp[a + 1];
        for i in range(index + 1, len(exp)):
            if (exp[i] == '+' or exp[i] == '-' or exp[i] == '*' or exp[i] == '/'):
                b = i;
        eIndex = exp[b];
        x = exp[a + 1:index];
        y = exp[index + 1:b];
        ans = int(x) - int(y);
        exp1 = exp[sIndex:eIndex];
        exp = exp.replace(exp1, str(ans));
        print(exp);
        print(len(exp));

print(f"Result : {exp}");