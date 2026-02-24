import math
def check_prime(i:int):
    tb = math.sqrt(i)
    tb = int(tb)
    checkn = 0
    if ( i == 2):
            checkn = 1
    elif( i % 2 != 0 ):
        for j in range (2,tb+1):
            if ( i % j == 0):
                checkn = 0
                break
            else: 
                checkn = 1
                continue
    return checkn            
        

n = input("Enter one integer number: ")
try: 
    n = int(n)
except: 
    print('This is no a integer number! Please enter again! ')

if ( check_prime(n) == 1):
    print('This is a prime number')
else:
    print('This is not prime number')