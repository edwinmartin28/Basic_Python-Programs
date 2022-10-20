# Write a Python program to find the union and intersection of two lists.
a=list()
b=list()
c=list()
d=list()

n = int(input("Enter the number of elements in first list:"))
print("Enter the elements to list 1")
for i in range(n):
    x = int(input("Element "+str(i+1)+" : "))
    a.append(x)
print("list 1:",a)

n = int(input("Enter the number of elements in second list:"))
print("Enter the elements to list 2")
for i in range(n):
    x = int(input("Element "+str(i+1)+" : "))
    b.append(x)
    
print("list 2:",b)
for x in a :
    if(x in b and x not in c):
        c.append(x)
        
for i in a :
    if(i not in d):
        d.append(i)
       
for x in b :
    if(x not in d):
        d.append(x)
   
print("\nUnion is : ",d)
print("Intersection is : ",c)