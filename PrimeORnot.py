#Python program to check weather a given numbers is prime or not .
x=int(input("Enter a number:"))
for i in range(2,int(x/2)):
	if x%i==0:
		print("The given number is not a prime number")
		exit(0)     
if x==1:
	print("The given number neither prime or composite number")
else:
	print("The given number is a prime number ")