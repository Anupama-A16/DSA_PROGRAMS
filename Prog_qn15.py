# Selection sort algorithm implementation in Python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if arr[j] < arr[min_i]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr
print("Enter the elements of the array separated by spaces:")
arr = list(map(int, input().split()))
print("Sorted array:", selection_sort(arr))