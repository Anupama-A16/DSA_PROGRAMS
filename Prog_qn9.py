# print 1 to n and n to 1 using recursion
def print_numbers(i, n):
    if i <= n:                     # 1 to n
        print(i)
        print_numbers(i + 1, n)    
print_numbers(1, 10) 
print("---------------------------------------------------")

def print_reverse_numbers(i, n):
    if i <= n:                     # n to 1
        print_reverse_numbers(i + 1, n)
        print(i)

print_reverse_numbers(1, 10)