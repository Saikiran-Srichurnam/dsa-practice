"""
    *
   ***
  *****
 *******
*********
"""

"""
treat the pattern like this instead of spaces consider what ever symbol you want before the stars
$$$$*
$$$***
$$*****
$*******
*********
"""
n = 5

for i in range(n):
  
  # first we have to print the spaces present before the stars
  for j in range(n-i-1):
    # print("$", end="")
    print(" ", end="")
  
  # print the stars
  for k in range(2*i+1):
    print("*", end="")
  print()