num = int(input("Enter the Number "))
print("Prime factor of given number is:")
i=2
while num>=1:
    while num%i==0:
        num //= i
        if num!=1:
           print(f"{i}",end="*")
        else:
            print(f"{i}")
        #num //= i

    i+=1    
        
