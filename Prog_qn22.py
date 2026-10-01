# Check if the array is sorted 

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by commas: ").split(",")))
is_sorted = True

for i in range(0, n-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

print("Is the array sorted in ascending order?", is_sorted)