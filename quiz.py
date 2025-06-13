while True:
    # Input validation for appliance type
    appliance_type = int(input("Enter appliance type (1-4): "))
    while appliance_type < 1 or appliance_type > 4:
        print("The appliance type you entered is not valid. Please try again.")
        appliance_type = int(input("Enter appliance type (1-4): "))

    # Input validation for sale price
    sale_price = float(input("Enter the sale price: "))
    while sale_price < 0:
        print("Sale price cannot be negative. Please enter a valid amount.")
        sale_price = float(input("Enter the sale price: "))
 
    # Calculate commission based on the given conditions
    if appliance_type == 1:
        commission = max(0.07 * sale_price, 400)
    elif appliance_type == 2:
        commission = min(0.10 * sale_price, 900)
    elif appliance_type == 3:
        commission = 0.12 * sale_price
    else:  # appliance_type == 4
        commission = 250

    # Output the commission
    print(f"The commission for this sale is: PHP {commission:.2f}")

    # Ask if the user wants to repeat
    repeat = input("Do you want to calculate another commission? (yes/no): ").strip().lower()
    if repeat != 'yes':
        print ("Thank you for using the program!")
        break