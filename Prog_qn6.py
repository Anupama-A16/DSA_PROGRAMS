# Store Frequency in Dictionary

#METHOD- 1
num= [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
freq_map = {}
for i in num:
    if i in freq_map:
        freq_map[i] += 1
    else:
        freq_map[i] = 1
print("Frequency of each element in METHOD-1: ", freq_map)


#METHOD- 2
num= [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5]
hash_map = {}
for i in range(len(num)):
    hash_map[num[i]] = hash_map.get(num[i], 0) + 1
print("Frequency of each element in METHOD-2: ", hash_map)