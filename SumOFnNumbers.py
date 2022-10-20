#Python program to find sum of n numbers.
N=int(input("Enter a limit:"))
Sum=0
for i in range(1,N+1):
    num=int(input("Enter number "+str(i)+" :"))
    Sum=Sum+num
print("Sum="+str(Sum))