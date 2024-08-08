num = int(input("Enter the Number for Calculating factorial"))
fact=1
for i in range(num):
    fact = fact*num
    num -= 1
print(fact)    
