#Python program to print words which are greater than a given length 'k'.
str1=input("Enter a string : ")
k=int(input("Enter value for k : "))
string=[]
text=str1.split()
for x in text:
 if len(x) > k:
  string.append(x)
print("Words with length greater than "+str(k)+" are",end=" ")
print(string)
