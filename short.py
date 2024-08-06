lst = input("Enter intiger value seperated by space").split()
my_list = [int(s) for s in lst]
n = len(my_list)
for i in range(n):
  for j in range(n-i-1):
    if my_list[j]>my_list[j+1]:
      my_list[j] = my_list[j+1]+my_list[j]
      my_list[j+1] = my_list[j]-my_list[j+1]
      my_list[j] = my_list[j]-my_list[j+1]

print(my_list)

   



