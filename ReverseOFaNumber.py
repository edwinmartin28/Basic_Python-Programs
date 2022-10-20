#Python p[rogram to find reverse of anumber.
x=int(input("Enter a number:"))
r=0
while x!=0:
		d = int(x % 10)
		r = int((r*10) + d)
		x = int(x /10)
print("Reverse ="+str(r))
	