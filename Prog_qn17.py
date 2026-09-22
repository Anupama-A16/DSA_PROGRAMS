# Insertion sort algorithm implementation in Python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print("Enter the elements of the array separated by spaces:")
arr = list(map(int, input().split()))
print("Sorted array:", insertion_sort(arr))