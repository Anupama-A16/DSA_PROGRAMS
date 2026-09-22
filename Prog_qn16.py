# Bubble sort algorithm implementation in Python
def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(n-i-1):
            if  arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Enter the elements of the array separated by spaces:")
arr = list(map(int, input().split()))
print("Sorted array:", bubble_sort(arr))