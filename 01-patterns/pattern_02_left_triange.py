"""
*
**
***
****
*****
"""

n = 5 
for i in range(n):       # loop for rows
  for j in range(i+1):   # loop for columns: number of stars = row number + 1
    print("*", end="")
  print()