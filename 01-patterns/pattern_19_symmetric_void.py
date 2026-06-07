"""
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""

n=5

for i in range(n):
    for j in range(n-i):
        print("*", end="")
        
    print(" "*(2*i), end="")
    
    for k in range(n-i):
        print("*", end="")
    print()
    
for i in range(n):
    for j in range(i+1):
        print("*", end="")
        
    print(" "*(2*(n-i-1)), end="")
    
    for k in range(i+1):
        print("*", end="")
    print()