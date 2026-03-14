def sum_lst(s:list):
    n = len(s)
    r = []
    for i in range (0,n):
        if ( s[i] % 2 == 0):
            r.append(s[i])
    return r

lst = [17, 4, 29, 8, 13, 42, 6, 25, 11]
print(lst)
print(f"{sum_lst(lst)}")