#find matching character in two string and count matching character
string_1 = input("Enter a string1: ")
string_2 = input("Enter a string2: ")
my_string_list_1 = [(e) for e in string_1]
my_string_list_2 = [(e) for e in string_2]
n1 = len(my_string_list_1)
n2 = len(my_string_list_2)
new_list = []

for i in range(n1):
    for j in range(n2):
        if my_string_list_1[i]==" ":
            continue
        elif my_string_list_1[i] == my_string_list_2[j]:
            if my_string_list_1[i] in new_list:
                pass
            else:
                new_list.append(my_string_list_1[i])
            
            
print(new_list)
print(f"Total number of matching character is {len(new_list)}")