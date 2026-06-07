"""
A B C D E
A B C D
A B C
A B
A
"""

n = 5
for i in range(n):
    for j in range(n-i):
        print(chr(65 + j), end="")
    print()
    