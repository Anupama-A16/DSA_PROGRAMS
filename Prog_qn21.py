# Find second largest number in the array, array can contain negative numbers as well
n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
largest = arr[0]
second_largest = arr[0]

for i in range(0, n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("The second largest number in the array is:", second_largest)