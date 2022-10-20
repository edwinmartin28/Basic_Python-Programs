#Python program to create a arithematic calculator.
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print("1 for Addition\n2 for Substraction\n3 for Division\n4 for Multiplication")
z=int(input("Enter your choice :"))
if z==1:
  print("Sum="+str(x+y))
elif z==2:
  print("Difference="+str(x-y))
elif z==3:
  print("Quotent="+str(x/y))
elif z==4: 
  print("Product="+str(x*y))
 
