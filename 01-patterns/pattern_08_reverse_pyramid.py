"""
*********
 *******
  *****
   ***
    *
    
treat the pattern like this instead of spaces consider what ever symbol you want before the stars

*********
$*******
$$*****
$$$***
$$$$*
"""
n=5

for i in range(n):
  
  #print spaces first as per our observation the spaces are printed according to the i value
  # if i = 0 then 0 spaces, i = 1 then 1 space and so on
  for j in range(i):
    # print("$", end="")
    print("#", end="")
    
  for k in range(2*(n-i) - 1):
    print("*", end="")
  print()