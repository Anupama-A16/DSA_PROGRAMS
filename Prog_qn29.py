# Find maximum consecutive ones in an array

num = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1]
count = 0
max_count = 0

for i in range(len(num)):
    if num[i]==1:
        count +=1
    else:
        max_count = max(max_count, count)
        count = 0
print("Maximum consecutive ones: ", max(max_count, count))