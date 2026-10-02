# Remove Duplicates from a Sorted Array
n = int(input("Enter the number of elements in the sorted array: "))
arr = list(map(int, input("Enter the elements of the sorted array separated by spaces: ").split()))

i = 0
j = i+1

while j< n:
    if arr[i] != arr[j]:
        i +=1
        arr[i], arr[j] = arr[j], arr[i]
    j +=1
print("The array after removing duplicates is:", arr[:i+1])
