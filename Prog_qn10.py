# sum of 1 to n using functional recursion
def sum_of_numbers(i, n):
    if i <= n:
        return i + sum_of_numbers(i + 1, n)
    else:
        return 0

print(sum_of_numbers(1, 10))

# sum of 1 to n using parameterized recursion
def sum_of_numbers_param(i, n, sum):
    if i > n:
        print(sum)
        return 
    sum_of_numbers_param(i + 1, n, sum+i)
sum_of_numbers_param(1, 3, 0)
    