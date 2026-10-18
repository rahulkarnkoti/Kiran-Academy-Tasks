import random

while True:
    print("\n1. Book Ride")
    print("2. Exit")
    choice = input("Enter choice: ")

    if choice == "2":
        print("Goodbye!")
        break

    elif choice == "1":
        # Choose cab
        print("\n1. Auto (12/km)")
        print("2. Sedan (18/km)")
        print("3. SUV (25/km)")
        cab = input("Choose cab: ")

        if cab == "1":
            cab_name = "Auto"
            rate = 12
        elif cab == "2":
            cab_name = "Sedan"
            rate = 18
        elif cab == "3":
            cab_name = "SUV"
            rate = 25
        else:
            print("Invalid cab choice")
            continue

        # Choose route
        print("\n1. Pune Station to Shivajinagar (5 km)")
        print("2. Pune Station to Kothrud (10 km)")
        print("3. Pune Station to Wakad (19 km)")
        print("4. Swargate to Shivajinagar (7 km)")
        print("5. Swargate to Kothrud (9 km)")
        print("6. Swargate to Wakad (21 km)")
        print("7. Hinjawadi to Shivajinagar (18 km)")
        print("8. Hinjawadi to Kothrud (15 km)")
        print("9. Hinjawadi to Wakad (6 km)")
        
        route = input("Choose route: ")

        if route == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route == "2":
            source = "Pune Station"
            destination = "Kothrud"
            distance = 10
        elif route == "3":
            source = "Pune Station"
            destination = "Wakad"
            distance = 19
        elif route == "4":
            source = "Swargate"
            destination = "Shivajinagar"
            distance = 7
        elif route == "5":
            source = "Swargate"
            destination = "Kothrud"
            distance = 9
        elif route == "6":
            source = "Swargate"
            destination = "Wakad"
            distance = 21
        elif route == "7":
            source = "Hinjawadi"
            destination = "Shivajinagar"
            distance = 18
        elif route == "8":
            source = "Hinjawadi"
            destination = "Kothrud"
            distance = 15
        elif route == "9":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 6
        else:
            print("Invalid route choice")
            continue

        # Fare
        fare = rate * distance
        print("\nCab:", cab_name)
        print("From:", source)
        print("To:", destination)
        print("Distance:", distance, "km")
        print("Rate:", rate, "per km")
        print("Total Fare:", fare)

        # Confirm or cancel
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")
        confirm = input("Enter choice: ")

        if confirm == "1":
            otp = random.randint(1000, 9999)
            print("Your OTP is:", otp)
            print("OTP shared. Ride can NOT be cancelled now.")
            print("Booking Confirmed!")
        elif confirm == "2":
            print("Ride cancelled.")
        else:
            print("Invalid choice")

    else:
        print("Invalid choice, try again")