
try:
    inches = float(input("Enter inches : "))
    while inches >= 0:
            centimeters = inches / 0.39370
            print(inches, "(inch) =", f"{centimeters:3.f}", "(cm)")
            inches = float(input("Enter inches : "))
    print("ENDING FOR CONVERTING.") 
except ValueError:
        print('The input did not a number! Please, enter again!!!')