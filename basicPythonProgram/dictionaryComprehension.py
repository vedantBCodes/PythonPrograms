
# Dictionary comprehesion using expression

my_dic={x:x**2 for x in range(5)};

print(my_dic);

# Dictionary comprehesion using condition (filtering)

my_dic2={x:x**2 for x in range(5) if(x%2==0)};

print(my_dic2);

my_dic3={x:('odd' if x%2==1 else 'even') for x in range(5) };

print(my_dic3);

# Dictionary comprehesion using function
def evenOdd(num):
    if(num%2==0):
        return 'even';
    else:
        return 'odd';

list5={x:evenOdd(x) for x in range(5)};

print(list5);
