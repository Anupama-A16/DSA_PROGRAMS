# Find largest number in the array, array can contain negative numbers as well

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
    
print("The largest number in the array is:", largest)