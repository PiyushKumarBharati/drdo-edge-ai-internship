def temp_converter():
    print("Temperature Converter")
    choice = input("Convert to (C/F): ").upper()
    temp = float(input("Enter temperature: "))

    if choice == "C":
        print("Result:", (temp - 32) * 5/9, "°C")
    elif choice == "F":
        print("Result:", (temp * 9/5) + 32, "°F")
    else:
        print("Invalid choice!")

temp_converter()
