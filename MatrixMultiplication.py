# Write a Python program to multiply two matrices.
matrix1=[]
matrix2=[] 
matrix3=[]
R1=int(input("Enter no of rows in matrix 1   : "))
C1=int(input("Enter no of columns in matrix 1: "))
R2=int(input("Enter no of rows in matrix 2   : "))
C2=int(input("Enter no of columns in matrix 2: "))
if C1==R2:
  print("Enter elements to matrix1: ")
  for i in range(R1):
      temp=list()
      for j in range(C1):
          temp.append(int(input()))
      matrix1.append(temp)  
  print("Enter elements to matrix2: ") 
  for i in range(R2):
      temp=list()
      for j in range(C2):
          temp.append(int(input()))
      matrix2.append(temp)  
  for i in range(R1):
      temp=list()
      for j in range(C2):
          temp.append(0)
      matrix3.append(temp)
  print("Matrix1:")
  for i in range(R1):
      for j in range(C1):
          print(matrix1[i][j], end = " ")
      print()
  print("Matrix2:")
  for i in range(R2):
      for j in range(C2):
          print(matrix2[i][j], end = " ")
      print()
  for i in range(R1):
      for j in range(C2):
          for k in range(C1):
              matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
  print("Product Matrix:")
  for i in range(R1):
      for j in range(C2):
          print(matrix3[i][j], end = " ")
      print()
else:
  print("Multiplication is not possible!")