PI = 3.14
import math

def unit_pizza(d : float, p : float):
    d = d/100
    dientich = pow((d/2),2) * PI
    p_unit = p / dientich
    return p_unit

while True:
    try:
        d1 = float(input('\nEnter the diameter(in centimeters) of the first pizza: '))
        p1 = float(input('Enter the price(USD) of the first pizza: '))
        d2 = float(input('\nEnter the diameter(in centimeters) of the second pizza: '))
        p2 = float(input('Enter the price(USD) of the second pizza: '))

        if ( unit_pizza(d1,p1) < unit_pizza(d2,p2) ):
            print('\nThe first pizza provides better value for money. ')
            break
        elif ( unit_pizza(d1,p1) > unit_pizza(d2,p2)):
            print('\nThe second pizza provides better value for money. ')
            break
        elif ( unit_pizza(d1,p1) == unit_pizza(d2,p2)):
            print('\nThe both pizzas provide the same value for money. ')
            break
    except ValueError:
        print('\nAt least one value has been entered incorrectly! Please re-enter it from the beginning!')

