"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    
treat the problem as 4 parts

 - first print the spaces         -- |
                                     |  pyramid pattern 
 - print the stars after spaces   -- | 
 
 - print spaces then              -- |
                                     |  reverse pyramid pattern 
 - print stars                    -- |
 
so this problem is combination of pyramid and reverse pyramid pattern 

"""

n = 5
for i in range(n):
  for j in range(n-i-1):
    print(" ", end="")
    
  for k in range(2*i + 1):
    print("*", end="")
  print()
  
for i in range(1,n): #  # start from 1 to avoid duplicate middle row
  for j in range(i):
    print(" ", end="")
  
  for k in range(2*(n -i) -1):
    print("*", end="")
  print()