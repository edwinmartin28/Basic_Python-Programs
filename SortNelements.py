#Python program to sort N elements using bubble sort.
def sort(list):  
    for i in range(0,len(list)-1):  
        for j in range(len(list)-1):  
            if(list[j]>list[j+1]):  
                temp = list[j]  
                list[j] = list[j+1]  
                list[j+1] = temp  
    return list  
list = []
n = int(input("Enter the number :"))
print("Enter the elements to list")
for i in range(n):
    x = int(input("Enter number "+str(i+1)+" :"))
    list.append(x)
print("Unsorted list is: ", list)  
print("Sorted list is: ", sort(list)) 