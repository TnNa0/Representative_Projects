#Collections
############

#3.1
print("\nExercise 3.1\n")

def set_def(m):
            
    M = set()
    for n in range(10 + 1):
        i = n * m
        M.add(i)
        if n == 0:
            M.pop()
    
    print(f"{M}M{m}")
    return (M)

m = [4, 6, 9]
allM = {"M4" : [], "M6": [], "M9": []}
uniqueM = {"uM4" : [], "uM6": [], "uM9": []}
two_but_not_third = {"M4uM6" : [], "M4uM9": [], "M6uM9": []}
interM = {"inter" : []}

for n in m:
    if n == 4:
        allM["M4"] = set_def(n)
    elif n == 6:
        allM["M6"] = set_def(n)
    else:
        allM["M9"] = set_def(n)

print("\nFull set collection", allM)

uniqueM["uM4"] = allM["M4"] - allM["M6"] - allM["M9"]
uniqueM["uM6"] = allM["M6"] - allM["M4"] - allM["M9"]
uniqueM["uM9"] = allM["M9"] - allM["M4"] - allM["M6"]

two_but_not_third["M4uM6"] = allM["M4"] & allM["M6"] - allM["M9"]
two_but_not_third["M4uM9"] = allM["M4"] & allM["M9"] - allM["M6"]
two_but_not_third["M6uM9"] = allM["M6"] & allM["M9"] - allM["M4"]

interM["inter"] = allM["M4"] & allM["M6"] & allM["M9"]

print("\nUnique", uniqueM)

print("\nTwo but not third", two_but_not_third)
print("\n Interesect all three", interM)
    

#3.2
print("\nExercise 3.2\n")


num = [i for i in range(27)]
alph_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
alph_list.insert(0, " ")
print("My lists used for the encryption dict:\n", num, alph_list)

encryption_table = {key: val for key, val in zip(alph_list, num)}
print("Encryption Table", encryption_table)


message = "THE FOOTBALL WAS DELIVERED"
encrypted_message = []

# for i in message:
#     for key, value in encryption_table.items():
#         if i == key:
#             encrypted_message.append(value)

encrypted_message = [encryption_table[i] for i in message]
print("Encrypted Message:\n", encrypted_message)

#3.3
print("\nExercise 3.3\n")

rev_encryption_table = dict((v, k) for k, v in encryption_table.items())
print("Reverse", rev_encryption_table)

code_message = [1, 12, 12, 0, 25, 15, 21, 18, 0, 2, 1, 19, 5, 0, 1, 18, 5, 0, 2, 5, 12, 15, 14,
7, 0, 20, 15, 0, 21, 19]
decrypted_message = [rev_encryption_table[i] for i in code_message]

# for i in code_message:
#     for key, value in rev_encryption_table.items():
#         if i == value:
#             decrypted_message.append(key)



print("Decrypted MEssage:\n", decrypted_message)

