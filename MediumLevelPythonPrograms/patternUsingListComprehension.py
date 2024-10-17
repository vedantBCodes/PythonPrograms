"""

*
* *
* * *
* * * *
* * * * *

"""

n=5;

[print('*' * i) for i in range(n+1)];

"""
        *
      * *
    * * *
  * * * *
* * * * *

"""

n=5;

[ print((' ' * (i)) + ('*' * (n-i))) for i in range(n,-1,-1) ];

