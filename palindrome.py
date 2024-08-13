#Check given number is palindrome or Not!
n = int(input("Enter a number"))

def check_plindrome(n):
  str_n = str(n)

  return str_n == str_n[::-1]

print(check_plindrome(n))
