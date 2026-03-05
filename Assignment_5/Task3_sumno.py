import re

def sum_numbers(text):
    numbers = re.findall(r'\d+', text)  
    total = 0
    
    for n in numbers:
        total += int(n)
        
    return total

s = input()
print(sum_numbers(s))