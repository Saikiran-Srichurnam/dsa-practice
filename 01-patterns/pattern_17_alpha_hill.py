"""
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""

n = 5
for i in range(n):
    print(" " * (n-i-1), end="")
    
    breakpoint = (2*i+1)//2
    ch = ord('A')
    for j in range(1,2*i+2):
        print(chr(ch), end="")
        if j <= breakpoint:
            ch += 1
        else:
            ch -=1
    
    print(" "*(n-i-1), end="") # to maintain symmetry from both sides
    print()