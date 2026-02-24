lst = []
while True:
    city = input("Enter a name of cities on the world: ")
    try: 
        city = int(city)
        break
    except:
        if ( city == ''):
                print
                break
        lst.append(city)
        continue
    
n = len(lst)
for i in range (0, n):
    print(lst[i])