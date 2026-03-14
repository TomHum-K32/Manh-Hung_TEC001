
month = input("Enter a number of month: ")
my_tuple = ("spring", "summer", "autumn", "winter")

try:
    month = int(month)
    if ( month == 1 or month == 2 or month == 12):
        print(my_tuple[3])
    elif ( month == 3 or month == 4 or month == 5):
        print(my_tuple[0])
    elif ( month == 6 or month == 7 or month == 8):
        print(my_tuple[1])
    elif ( month == 9 or month == 10 or month == 11):
        print(my_tuple[2])
    else:
        print("The entered number is not a number of month")
except:
    print("The wrong entered value! Please enter again @!!! ")

