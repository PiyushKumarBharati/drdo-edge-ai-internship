def calculator():
    print("Simple Calculator")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            try:
                print("Result:", num1 / num2)
            except ZeroDivisionError:
                print("Error: Division by zero!")
        else:
            print("Invalid operation!")

    except ValueError:
        print("Error: Please enter valid numbers.")

calculator()
