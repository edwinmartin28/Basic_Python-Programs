#Python program to print grade of a student by reading 3 subjects mark.
x=int(input("Mark 1:"))
y=int(input("Mark 2:"))
z=int(input("Mark 3:"))
avg=(x+y+z)/3
if avg>=90:
    print("Grade A")
elif avg>=80:
    print("Grade B")
elif avg>=70:
    print("Grade C")
elif avg>=60:
    print("Grade D")
elif avg>=50:
    print("Grade E")
else:
    print("Failed!")