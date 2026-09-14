# Armstrong Number
num = int(input("Enter a number: "))
original = num 
sum = 0 
while num > 0:
    digit = num%10
    sum+= digit**len(str(original))
    num//=10

if sum == original:
    print(original, "is an Armstrong number")
else: 
    print(original, "is not an Armstrong number")