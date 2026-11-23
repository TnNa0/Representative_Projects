#2.1
print("\n###### EXERCISE 2.1 ###########\n")

def ex_2_1(n):
    result_sum = 0.0
    for i in range(n + 1):
        result_sum += i ** 2
    print("My result:", result_sum)

def ctrl(n):
    result = n * (n + 1) * (2 * n + 1) / 6
    print("Ctrl result:", result)

input = [5, 42, 123]
for i in input:
    a = ex_2_1(i)
    b = ctrl(i)
    if a == b:
        print("True\n")
    else:
        print("False\n")

#ex 2.2
print("\n###### EXERCISE 2.2 ###########\n")

def ex_2_2(word):
    c = 0
    flag = 0
    for i in range(len(word) - 1):
        current = word[i]
        next = word[i + 1]
        if flag == 1:
            flag = 0
            continue
        if current == "t" and next != "h":
            flag = 1
            continue
        if current == "h":
            c += 1
                
    print(f">{word}< has {c} non-t succeeding h's")

words = ["through", "house", "knight", "wind", "that house is high", "hat"]
for i in (words):
    ex_2_2(i)            
        

#ex 2.3
print("\n##### EXERCISE 2.3 ############\n")


def ex_2_3(text):
    is_palindrom = True
    length = len(text)

    for i in range(length // 2):
        counter_i = (-1 - i)
        if text[i] != text[counter_i]:
            is_palindrom = False
            break
    print(f"Is >{text}< a palindorm?:", is_palindrom)

list_of_palindroms = ["level", "madame", "tacocat"]

for i in list_of_palindroms:
    ex_2_3(i)
