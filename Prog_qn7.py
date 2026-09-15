# given two lists of numbers where values in n<=10, values in m can be any number.
# find the frequency of each number in n also present in m. 
# If a number in n is not present in m, then its frequency should be 0.

n = [2,5,10,5,2,6,8]
m= [101, 290, 10, 2, 5]
hash_list = [0] * 11  # Index 0 to 10
for i in n: 
    hash_list[i] += 1
for j in m:
    if j <1 or j>10:
        print(j,":", 0)
    else:
        print(j,":", hash_list[j])