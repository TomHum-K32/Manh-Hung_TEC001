def leap_year():
    while True: 
        try:
            year = int(input("\nEnter a random year: "))
            if ( year > 0 ):
                if ( year % 400 == 0 or (year % 4 == 0 and year % 100 != 0 )):
                    print('\nThe year entered is a leap year.')
                    break
                else:
                    print('\nThe year entered is a normal year.')
            else:
                print('\nThe year entered does not exist! Please enter other year!')
        except ValueError :
            print('\nThe year entered does not exist! Please enter other year!')

leap_year()