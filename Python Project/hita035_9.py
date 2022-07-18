# To calculate total number of positive numbers, negative numbers, even and odd numbers and zeroes in a list

# Creating an empty list
l = []

# Taking list elements as input from the user
l = [int(item) for item in input("Enter the list items : ").split()]

# Initializing count values
cp=0
cn=0
co=0
ce=0
cz=0

# For counting positive numbers
for i in l:
    if i > 0:
        cp+=1
print(f"Total number of positive numbers is {cp}; since zero is neither positive nor negative")

# For counting negative numbers
for i in l:
    if i<0:
       cn+=1
print(f"Total number of negative numbers is {cn}")

# For counting even and odd numbers
for i in l:
    if i%2==0:
        ce+=1
    else:
        co+=1
print(f"Total number of even numbers is {ce}")
print(f"Total number of odd numbers is {co}")

# For counting number of 0s
for i in l:
    if i==0:
        cz+=1
print(f"Total number of 0s numbers is {cz}")



