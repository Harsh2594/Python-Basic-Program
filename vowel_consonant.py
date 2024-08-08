my_string = input("Enter the string: ")
vowel_list = ['a','e','i','o','u']
no_vowel = 0
no_conso = 0

for e in my_string:
  if e in vowel_list:
    no_vowel += 1  
  elif e == ' ':
    continue  
  else:
    no_conso += 1

print(f"Number of vowel in string is {no_vowel} and number of consonant is {no_conso}")    

