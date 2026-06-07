"""
E
DE
CDE
BCDE
ABCDE
"""

n=5

for i in range(n):
    ch = ord('E') - i
    for j in range(i+1):
        print(chr(ch+j), end="")
    print()