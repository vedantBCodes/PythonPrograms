PI=3.14;

def simpleInterest(p,n,r):
    si=(p*n*r)/100;
    return si;

def areaOfCircle(r):
    area=PI*r*r;
    return area;

def areaOfRectangle(l,b):
    area=(l*b);
    return area;

def areaOfTriangle(b,h):
    area=(b*h)/2;
    return area;

print(simpleInterest(1000,2.5,2));