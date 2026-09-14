# Print All Factors of a Given Number 
n = int(input("Enter a number: "))

from math import sqrt
print("Factors of", n, "are:")

result = []

for i in range(1, int(sqrt(n)) + 1):
    if n%i ==0:
        result.append(i)
        if i != n//i:
            result.append(n//i)
result.sort()
print(result)