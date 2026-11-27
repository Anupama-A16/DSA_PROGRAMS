# Find longest consecutive sequence in an unsorted array of integers.

arr = [100, 5, 3, 101, 2, 90, 98, 1, 99]
longest_streak = 0
my_set = set(arr)

for i in range(len(arr)):
    if arr[i] - 1 not in my_set:
        current_num = arr[i]
        current_streak = 1

        while current_num + 1 in my_set:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

print("The length of the longest consecutive sequence is:", longest_streak)
