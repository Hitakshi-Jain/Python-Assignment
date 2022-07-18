# 4x4 Matrix Multiplication by taking matrix as input from the user

# Initializing the matrices
A = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

B = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

#Intitializing resultant matrix
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

#Taking first matrix elements from the user
print('Please enter the entries for Matrix A row-wise: ')
for i in range(0, 4):
    for j in range(0, 4):
        A[i][j] = int(input())

##Taking second matrix elements from the user
print('Please enter the entries for Matrix B row-wise: ')
for i in range(0, 4):
    for j in range(0, 4):
        B[i][j] = int(input())

#printing the resultant matrix
print("The resultant matrix [matrix A x matrix B]: ")

for i in range(0, 4): #start of for loop
    for j in range(0, 4): #start of second for loop
        for k in range(0, 4): #start of third for loop
            result[i][j] += A[i][k] * B[k][j] #inside third for loop

#To get the resultant matrix in matrix form
        print(result[i][j], end=" ")     #inside second for loop
    print() #inside first for loop