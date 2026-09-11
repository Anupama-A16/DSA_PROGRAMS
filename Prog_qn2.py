# Count the Number of Digits in an Integer
n = int(input("Enter the number: "))
count = 0
while n>0:
    n//=10
    count+=1
print("Number of digits:", count)