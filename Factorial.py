#Python program to find factorial of anumber.
def factorial(num):
    fact=1
    for i in range(1, num+1):
        fact=fact*i
    return fact     
n=int(input("Enter a number:"))
result=factorial(n)
print("The factorial of %d = %d"%(n,result))
