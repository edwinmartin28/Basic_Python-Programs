#Python program to find the cube of number.
def cube(num):
    num=num*num
    return num   
n=int(input("Enter a number:"))
result=cube(n)
print("Cube of %d is %d"%(n,result))