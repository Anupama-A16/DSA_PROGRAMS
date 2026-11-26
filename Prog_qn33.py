# Rearrange the array elements by signs- opposite signs should be placed next to each other. 
# The order of positive and negative numbers should be maintained.

arr = [1, 3, -2, -4, -1, 4, 2]
rearranged = [0] * len(arr)
positive = 0
negative = 1

for i in range(len(arr)):
    if arr[i] >= 0:
        rearranged[positive] = arr[i]
        positive += 2
    else:
        rearranged[negative] = arr[i]
        negative += 2

print("The rearranged array is:", rearranged)