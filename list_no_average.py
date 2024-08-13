my_list = list(map(int,input("Enter list number separated by space").split()))
n = len(my_list)

def find_average(my_list):
  sum = 0
  for i in my_list:
    sum += i
  average = round(sum/n,2)
  return average  

print(f"Average of given list number is {find_average(my_list)}")