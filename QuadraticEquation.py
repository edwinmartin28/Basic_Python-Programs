#Python program to calculate roots of a quadratic equation. 
from cmath import sqrt
a= int(input("Enter value of a : "))
b= int(input("Enter value of b : "))
c= int(input("Enter value of c : "))

if(a==0):
    print("Not a Quadratic Equation")
    exit(0) 

r1=((-b+sqrt(pow(b,2)-4*a*c))/(2*a))
r2=((-b-sqrt(pow(b,2)-4*a*c))/(2*a))

print("Roots are : "+str(r1)+","+str(r2))