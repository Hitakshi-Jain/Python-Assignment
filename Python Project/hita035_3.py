# To display Pascal's triangle for n rows

# Taking n value from user
n = int(input("Enter n value: "))
for i in range(n):
    for j in range(n-i+1):

# for left spacing
        print(end=" ")

#To print the Pascal's Triangle using the algorithm nCr = n!/((n-r)!*r!)
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

# for new line
    print()




