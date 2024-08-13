#find Smallest number on left of list element
lst = list(map(int,input("Enetr the number").split()))
n = len(lst)

def nearest_smaller_toleft(lst):
  result = []

  for i in range(n):
    for j in range(i-1,-1,-1):
       if lst[i] > lst[j]:
         result.append(lst[j])
         break
    else:
      result.append(-1) 
  return result     
  
print(nearest_smaller_toleft(lst))