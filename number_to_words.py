number = int(input("Enter number less than 1000: "))
def number_to_words(n):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    if 0<= n <10:
        return ones[n]
    elif 10 < n < 20:
        return teens[n-11]
    elif 20 <= n < 100:
        return tens[n//10-1] + ('' if n%10 == 0 else '-'+ ones[n%10])
    elif 100 <= n < 1000:
        return ones[n//100]+' hundred '+tens[(n%100)//10-1]+' '+ones[(n%100)%10]
    else:
        return 'Number out of range'
        
result = number_to_words(number)
print(result)