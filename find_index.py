#find index of two list element whose sum is given:
l = list(map(int,input("Enter the number separated by space").split()))
n = len(l)
sum = int(input("Enter the sum"))
result = []
for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j] == sum:
            result.append(i)
            result.append(j)
            
    
print(result)        
        
            
        




    
                

    