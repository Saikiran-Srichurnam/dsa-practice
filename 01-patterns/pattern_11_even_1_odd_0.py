"""
1
01
101
0101
10101

if we observe clearly we understand that if the sum of i+j is even then print 1 otherwise print 0
"""
n = 5
for i in range(n):
  for j in range(i+1):
    if (i+j) % 2 == 0:
      print("1", end="")
    elif (i+j) % 2 != 0:
      print("0", end="")
  print()
