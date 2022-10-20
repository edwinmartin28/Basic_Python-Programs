#Python program to count the occurrences of each word in a given sentence.
str=input("Enter a scentence : ")
str = str.split()        
str2 = []

for i in str:            
    if i not in str2:
        str2.append(i)
for i in range(len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))
