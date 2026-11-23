# Exercise 1.1

'''
Make yourself comfortable with the integrated development environment Spyder 
(or any other coding editor of your choice). Open your program and start an 
empty Python document. Print the string "Hello World!" on the console.

You can decide which IDE / editor you want to use for the rest of this course.
'''

print("Exercise 1:\nHello World!\n")




# Exercise 1.2

'''
We are given two points S = (x1 / y1) and E = (x2 / y2) within a mathematical 
coordinate system. We are searching the plane

P: y = mx + n

which intersects the points S and E.

Reminder: the equations for calculating the slope m and the intercept n are:

m = (y2 - y1) / (x2 - x1)
n = y - mx

Find the parameters m and n for the points:
S = (-1 / -4)
E = (3 / 28)

Print the results in the console.
'''
x1 = -1
y1 = -4

x2 = 3
y2 = 28

S = (x1, y1)
E = (x2, y2)


#  m = (y2 - y1) / (x2 - x1)
m = ((E[1]-S[1]) / (E[0]-S[0]))
# n = y - m*x
nS = S[1] - m *S[0]
nE = E[1] - m * E[0]


print(f"Excercise 2\nm is {m}\nn for S is {nS} and n for E is {nE}\n")


# Exercise 1.3

'''
Manipulate the following strings as described:

• Create a string consisting of the characters with index
  3, 5, 7, 9, … of the string "Multiomics Data Science"
  using slicing.

• Create the reverse string of the sequence
  "never odd or even" using slicing.

• Replace all occurrences of the string "he" with "she"
  in the string:
  "Today he was hearing heavy metal in the chemistry class."

Print all results into the console.
'''

my_string = "Multiomics Data Science"
string2 = "never odd or even"
string3 = "Today he was hearing heavy metal in the chemistry class."
print("Excercise 3")
print(my_string[3::2])
print(string2[::-1])
print(string3.replace("he", "she"))
print("\n")

# Exercise 1.4

'''
The Gaussian Easter formula is used to compute the date of Easter Sunday.

As input, we write into the variable X the year we want to evaluate.
The output is the OS-th day in March.

In the formula:
div = integer division
mod = modulo operation

Rewrite the complete formula as Python code.

Calculate the dates for Easter Sunday for the years:
1984
2000
2026

by copy-pasting the code three times.

Source:
https://de.wikipedia.org/wiki/Gaußsche_Osterformel
'''

print("Exercise 4:")

years = (1984, 2000, 2026)

for X in years:
    K = X // 100
    M = 15 + (3 * K + 3) // 4 - (8 * K + 13) // 25
    S = 2 - (3 * K + 3) // 4
    A = X % 19
    D = (19 * A + M) % 30
    R = (D + A // 11) // 29
    OG = 21 + D - R
    SZ = 7 - (X + X // 4 + S) % 7
    OE = 7 - (OG - SZ) % 7
    OS = OG + OE

    print(f"In the year {X} easter will fall on {OS} of March")  


