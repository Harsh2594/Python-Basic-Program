series_len = int(input("How many number you want to print: "))
count = 1
n1 = 2
prime_list = []
while n1 >= 2:
    for i in range(2,n1-1):
        if n1%i==0:
            break
    else:
        prime_list.append(n1)
        count += 1    
    if count <= series_len:    
        n1 += 1
        continue
    else:
        break
print(prime_list)









