import myPackage.myMathModule as myMath

"""
One can also import the package like this -->from myPackage import myMathModule as myMath
"""

si=myMath.simpleInterest(1000,2.5,4);
print(f"Simple Interest : {si}");

aCircle=myMath.areaOfCircle(5);
print(f"Area of Circle : {aCircle}");

aTriangle=myMath.areaOfTriangle(5,10);
print(f"Area of Triangle : {aTriangle}");