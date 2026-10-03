# Right Rotate an Array by k Place

n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
k = int(input("Enter the number of places to rotate the array: "))

def right_rotate(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Perform right rotation by k places
k = k % n  # Handle cases where k is larger than the array size
right_rotate(arr, 0, n - 1)  # Reverse the entire array
right_rotate(arr, 0, k - 1)  # Reverse the first k elements
right_rotate(arr, k, n - 1)  # Reverse the remaining elements

print("Array after right rotation by", k, "places:")
print(arr)