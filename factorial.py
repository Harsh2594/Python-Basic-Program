num = int(input("Enter the Number for Calculating factorial"))
fact=1
for i in range(num):
    fact = fact*num
    num -= 1
print(fact)    

#Factorial using recursion:

n = int(input("Enter number: "))

def factorial(n):
    if n == 1:
        return n
    return factorial(n-1)*n
    
print(factorial(n))    
        
