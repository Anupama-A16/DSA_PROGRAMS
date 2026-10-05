# Merge two sorted arrays into one sorted array without duplicates

n1 = int(input("Enter the number of elements in the first sorted array: "))
arr1 = list(map(int, input("Enter the elements of the first sorted array separated by spaces: ").split()))
n2 = int(input("Enter the number of elements in the second sorted array: "))    
arr2 = list(map(int, input("Enter the elements of the second sorted array separated by spaces: ").split()))

result = []
i = j = 0

while i < n1 and j < n2:
    if arr1[i] < arr2[j]:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    elif arr1[i] > arr2[j]:
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1
    else:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
        j += 1

# Append any remaining elements from either array
while i < n1:
    if not result or result[-1] != arr1[i]:
        result.append(arr1[i])
    i += 1

while j < n2:
    if not result or result[-1] != arr2[j]:
        result.append(arr2[j])
    j += 1

print("Merged sorted array without duplicates:", result)