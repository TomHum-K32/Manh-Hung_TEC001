def sum_lst(s:list):
    n = len(s)
    tb = 0
    for i in range (0,n):
        tb += s[i]
    return tb

lst = [17, 4, 29, 8, 13, 42, 6, 25, 11]
print(f"{sum_lst(lst)}")