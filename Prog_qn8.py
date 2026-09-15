# given a string and a list of characters, 
# find the frequency of each character in the string that is also present in the list.

s = "programming"
l= ["m", "g", "z", "a", "k"]
dict_list = {}
for i in s:
    dict_list[i] = dict_list.get(i, 0) + 1
print("The frequency of each character in the string: ", dict_list)
print("The frequency of characters in the list also present in the string: ")
for j in l:
    if j in dict_list:
        print(j,":", dict_list[j])
    else:
        print(j,":", 0)