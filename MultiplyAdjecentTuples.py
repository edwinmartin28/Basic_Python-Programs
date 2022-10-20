#Python program to multiply adjecent elements in a tuple
n=int(input("Enter number of elements: "))
l=[]
for i in range(0,n):
    l.append(int(input()))
l=tuple(l)
for i in range(len(l)-1):
    print(l[i],"*",l[i+1],"=",l[i]*l[i+1])
