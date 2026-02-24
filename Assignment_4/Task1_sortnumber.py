def check_list(s:list):
    n = len(s)
    for i in range (0,n):
        for j in range (i+1,n):
            if ( s[i] < s[j] ):
                tsb = s[i]
                s[i] = s[j]
                s[j] = tsb
    return s

lst = []
while (True):
    i = input("Enter your number: ")
    try:
        i = float(i)
    except:
        print('End the step for entering number!')
        break
    lst.append(i)

check_list(lst)

for i in range (0,5):
    print(lst[i])