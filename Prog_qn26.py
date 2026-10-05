# Implementation of linear search algorithm in Python

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

target = int(input("Enter the target element to search for: "))

for i in range(n):
    if arr[i] == target:
        print("Element found at index:", i)
        break
else:
    print("Element not found in the array.")