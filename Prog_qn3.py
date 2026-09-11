# Check if a Number is Palindrome or Not
n = int(input("Enter the number: "))
rev = int(str(n)[::-1])
if n == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")