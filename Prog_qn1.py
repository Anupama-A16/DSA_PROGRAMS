# Extraction of Digits Using Loops

n = int(input("Enter the number: "))

while n>0:
    m= n%10
    print(m)
    n//=10