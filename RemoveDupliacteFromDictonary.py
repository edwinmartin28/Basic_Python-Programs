#Remove all duplicates values accross disctionaty values
n=int(input("Enter number of elements: "))
d=dict()
for i in range(0,n):
    k=input("Enter key: ")
    v=input("Enter value: ")
    d.update({k:v})
print(d)
d1=dict()
for key,val in d.items():
    if val not in d1.values():
       d1.update({key:val})
print(d1)