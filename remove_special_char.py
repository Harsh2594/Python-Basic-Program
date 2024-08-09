#Remove special character in lowercase
my_string = input("Enter a string")
valid_char = 'abcdefghijklmnopqrstuvwxyz1234567890'
new_string = ''
def remove_special_char(s):
    global new_string
    for char in s:
        if char.lower() in valid_char:
            new_string += char.lower()
        
    return new_string

print(remove_special_char(my_string))    


