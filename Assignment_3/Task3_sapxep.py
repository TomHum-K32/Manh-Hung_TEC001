import math 
min = float('inf')
max = float('-inf')

while (True):
    i = input("Enter your number: ")
    try:
        i = float(i)
    except:
        print('End the step for entering number!')
        break
    if ( i <= min ):
        min = i
    if ( i >= max ):
        max = i
print('Max: ', max)
print('Min: ', min)
