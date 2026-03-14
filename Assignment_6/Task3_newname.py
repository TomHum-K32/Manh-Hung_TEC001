
names = set()

while True: 
    new_name = input("Enter a random name: ")
    if ( new_name == ""):
        break
    if new_name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(new_name)

print("\nName entered in here: ")
for new_name in names:
    print(new_name)