# Find the maximum sum of a contiguous subarray in the given array

n = (int(input("Enter the number of elements in the array: ")))
arr = list(map(int, input("Enter the numbers in the array separated by space: ").split()))

max = float('-inf')
total = 0

for i in range(n):
    total +=arr[i]
    if total > max:
        max = total
    if total < 0:
        total = 0

print("The maximum sum of a contiguous subarray is:", max)