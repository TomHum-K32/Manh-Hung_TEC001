def check_zander():
    length = float(input("Enter the length of the zander(cm): "))

    if ( length < 42):
        print("\nRelease the fish back into the lack!!!")
        print("The length of the fish that was caught deviated from the standard length by:", 42 - length, "cm" )
    else:
        print("\nThe length of the fish caught perfectly meets the standards for fishing.")

check_zander()