# reverse an array using recursion
def reverse_array(arr, start, end):
    if start>= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start + 1, end - 1)

a = [1, 2, 3, 4, 5]
reverse_array(a, 0, len(a) - 1)
print(a)