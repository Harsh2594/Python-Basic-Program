#find missing and dublicate number in given list.
my_list = [2,3,3,5,6,5,9]
last_no = my_list[-1]
missing_no = []


def find_missing_no():
  for i in range(1,last_no+1):
    if i in my_list:
      pass
    else:
      missing_no.append(i)
  return missing_no   
print(f"missing number in given list is {find_missing_no()}")

def dublicate_no():
  dublicate = []
  for i in range(len(my_list)):
    for j in range(i+1,len(my_list)):
      if my_list[i] == my_list[j] and my_list[i] not in dublicate:
        dublicate.append(my_list[i])
  return dublicate      

print(f"dublicate number in given list is {dublicate_no()}")