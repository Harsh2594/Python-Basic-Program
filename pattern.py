#pattern 1
for i in range(5):
  for j in range(i+1):
    print("*",end=" ")
  print()  

#pattern 2

for i in range(5):
  for j in range(5-i-1):
    print(" ",end = " ")
  for j in range(i+1):
    print("*",end = " ")
  print()      

#Up traingle

for i in range(1,6):
  for j in range(6-i-1):
    print(" ",end = " ")  
  for k in range(2*i-1):
    print("*",end = " ")  
  print()  

#down traingle

for i in range(5,0,-1):
  for j in range(0,5-i):
    print(" ",end = " ")
  for k in range(2*i-1):
    print("*",end = " ")  
  print()  
  