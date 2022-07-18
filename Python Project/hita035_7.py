# To sort the array and search the key element using different approaches

# Function for insertion sort
def insort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    print(f"Sorted array using insertion sort algorithm is {a}")

# Function for insertion sort
def sesort(a):
    length = len(a)
    for i in range(length-1):
        min = i
        for j in range(i+1, length):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

    print(f"Sorted array using selection sort algorithm is {a}")

# Function for binary search
def binary_search(a, key1):
    low = 0
    high = len(a) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if a[mid] < key1:
            low = mid + 1
        elif a[mid] > key1:
            high = mid - 1
        else:
            return mid+1
    return -1

# Function for binary search
def linear_search(a, key2):
    for i in range(len(a)):
        if a[i] == key2:
            return i+1
    return -1

# Driver input
a = []
n = int(input("Enter number of array elements : "))
print("Enter array elements")
for i in range(0, n):
    element = int(input())
    a.append(element)
print(f"The Unsorted array is: {a}")

# Calling the sorting functions
insort(a)
sesort(a)

# For Binary Search
key1 = int(input("Enter the key to search using Binary search algorithm: "))
binary_result = binary_search(a,key1)
if binary_result != -1:
    print("The Element is present at position", str(binary_result))
else:
    print("The Element is not present in array")

# For Linear Search
key2 = int(input("Enter the key to search using Linear search algorithm: "))
linear_result = linear_search(a,key2)
if linear_result != -1:
    print("The Element is present at position", str(linear_result))
else:
    print("The Element is not present in array")
