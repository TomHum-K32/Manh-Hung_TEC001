def check_cabin():
    try:
        print('\n============Table of class============')
        print('1. LUX')
        print('2. A')
        print('3. B')
        print('4. C')
        print('======================================')

        cabin = input("\nEnter the cabin class of a cruise ship: ")
        if ( cabin == "LUX"):
            print('\nThe position of LUX: upper-deck cabin with a balcony.')
        elif ( cabin == 'A'):
            print('\nThe position of A: upper-deck cabin with a balcony.')
        elif ( cabin == 'B'):
            print('\nThe position of B: upper-deck cabin with a balcony.')
        elif ( cabin == 'C'):
            print('\nThe position of C: upper-deck cabin with a balcony.')
    except ValueError:
        print('\nInvalid cabin class')

check_cabin()  
