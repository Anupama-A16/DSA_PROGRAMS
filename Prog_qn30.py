# Find the numbers in the array, whose sum is equal to the given number-target 
# and return the indices of those numbers

n = (int(input("Enter the number of elements in the array: ")))
arr = list(map(int, input("Enter the numbers in the array separated by space: ").split()))
target = int(input("Enter the target number: "))

hash_map = {}
for i in range(n):
    remaining = target - arr[i]
    if remaining in hash_map:
        print("Indices of the numbers whose sum is equal to the target: ", hash_map[remaining],"and", i)
        break
    hash_map[arr[i]] = i
    