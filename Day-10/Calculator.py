def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:                          # handle divide by zero
        print("Cannot divide by zero!")
        return None
    return a / b

a = float(input("Enter the first number: "))

calculating = True

while calculating:
    operation = input(
        "\nEnter the operation."
        "\n1) Press '+' for addition."
        "\n2) Press '-' for subtraction."
        "\n3) Press '*' for multiplication."
        "\n4) Press '/' for division.\n"
    )
    b = float(input("Enter the second number: "))

    if operation == "+":
        result = add(a, b)
        print(f"{a} + {b} = {result}")
    elif operation == "-":
        result = subtract(a, b)
        print(f"{a} - {b} = {result}")
    elif operation == "*":
        result = multiply(a, b)
        print(f"{a} * {b} = {result}")
    elif operation == "/":
        result = divide(a, b)
        if result is not None:
            print(f"{a} / {b} = {result}")
    else:
        print("Invalid operation. Please try again.")
        continue


    again = input(
        "\nTo continue with the result press y."
        "\nTo start a new calculation press n."
        "\nTo exit press q.\n"
    )

    if again == "y":
        a = result
    elif again == "n":
        a = float(input("Enter the first number: "))
    elif again == "q":
        print("Thank you for using this calculator.")
        calculating = False
    else:
        print("Invalid operation. Please try again.")
        break
