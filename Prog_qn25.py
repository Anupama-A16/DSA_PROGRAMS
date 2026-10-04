# move zeroes to the end of the array

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

def move_zeroes(arr):
    j = 0

    for i in range(n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr
print("Array after moving zeroes to the end:")
print(move_zeroes(arr))