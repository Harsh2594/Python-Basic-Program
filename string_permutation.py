my_string = input("Enter a string: ")
n = len(my_string)

def permute_string(my_string):
  if len(my_string) == 0:
    return []
  elif len(my_string) == 1:
    return [my_string] 
  
  permutations = []

  for i in range(len(my_string)):
    current = my_string[i]
    remaining = my_string[:i] + my_string[i+1:]

    for p in permute_string(remaining):
      permutations.append(current+p)
  return permutations    

permutations = permute_string(my_string)

print(f"total {len(permutations)} permutations are possible.")

for p in permutations:
  print(p)


   



