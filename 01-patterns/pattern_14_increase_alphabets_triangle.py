"""
A
A B
A B C
A B C D
A B C D E  
"""


n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(65 + j), end="")  # using the A ASCII value is 65 we have to print in a way that 65 + column number before printing we have to make them character using chr()
    print()
    