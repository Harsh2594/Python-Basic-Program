s = input("Enter any string you want to reverse")
n = len(s)
def reverse_string(s):
  if n == 1:
    return s
  return reverse_string(s[1:])+s[0]

reversed_string = reverse_string(s)
print(reversed_string)
