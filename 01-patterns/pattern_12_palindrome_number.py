"""
 1      1
 12    21
 123  321
 12344321
   
"""
n = 4

for i in range(1, n+1):    # rows from 1 to n
  for j in range(1, i+1):  # increasing numbers
    print(j, end="")
  
  for k in range(2*(n-i)): # middle spaces
    # print("_", end="")
    print(" ", end="")
  
  for m in range(i,0, -1): # decreasing numbers
    print(m, end="")
  print()