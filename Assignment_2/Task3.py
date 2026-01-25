def hemo_gender():
    print('\n============ Gender ============')
    print('1. Female')
    print('2. Male')
    print('==================================')
    
    while True:
        n = int(input("\nPlease, enter the choice number: "))

        if ( n == 1 ):
            hemo = float(input("Now, please enter your current hemoglobin value in your blood: "))
            if ( hemo < 117 ):
                print('\nYour curent hemglobin value in your blood is low.')
            elif ( hemo >= 117 and hemo <= 155):
                print('\nYour curent hemglobin value in your blood is normal.')
            elif ( hemo > 155):
                print('\nYour curent hemglobin value in your blood is high.')
            break
        elif ( n == 2):
            hemo = float(input('Now, please enter your current hemoglobin value in your blood: '))
            if ( hemo < 134 ):
                print('\nYour curent hemglobin value in your blood is low.')
            elif ( hemo >= 134 and hemo <= 167):
                print('\nYour curent hemglobin value in your blood is normal.')
            elif ( hemo > 167):
                print('\nYour curent hemglobin value in your blood is high.')
            break
        else:
            print('The choice was wrong! Please enter the number agian!!!!')

hemo_gender()