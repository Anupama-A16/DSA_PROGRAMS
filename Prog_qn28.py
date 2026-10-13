# Find Missing Number in an Array

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

for i in range(1, n + 1):
    if i not in arr:
        print("The missing number is:", i)
        break
    else:
        print("No missing number in the array.")