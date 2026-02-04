while True:
    n = input("Enter your number (inch): ")

    try:
        n = float(n)
    except:
        print("Please enter a valid number!")
        continue

    if n < 0:
        break

    centimeters = n / 0.39370
    print(n, "(inch) =", f"{centimeters:.3f}", "(cm)")

print("End the process!")
    
        
  


   
