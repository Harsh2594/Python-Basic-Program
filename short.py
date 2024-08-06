lst = input("Enter intiger value seperated by space").split()
my_list = [int(s) for s in lst]
n = len(my_list)
#Short list in increasing order
for i in range(n):
  for j in range(n-i-1):
    if my_list[j]>my_list[j+1]:
      my_list[j] = my_list[j+1]+my_list[j]
      my_list[j+1] = my_list[j]-my_list[j+1]
      my_list[j] = my_list[j]-my_list[j+1]

print(my_list)


#Reverse the given list
my_list2 = []
for i in range(n,0,-1):
  my_list2 = my_list2.append(my_list[i-1])
print(my_list2)  


#Find Second largest number 
print(my_list[-2])
   



