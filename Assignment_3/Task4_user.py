username = 'python'
password = 'rules'
i = 0
while True: 
    print('\n============ Account Login ============')
    name = input("Enter your username: ")
    word = input("Enter your password: ")
    print('=========================================')
    
    if ( name == username and word == password):
        print("Welcome")
        break
    else:
        print("Your username or password is incorrect! Please re-enter!")
        if ( i > 5):
            print("Access denied")
            break
    i += 1
