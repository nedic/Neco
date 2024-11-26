def calculate():
    while True:
        while True:
            try:
                number1 = float(input("Please enter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        operation = input("What operation do you want? (+, -, *, /): ").strip()
        while operation not in ["+", "-", "*", "/"]:
            operation = input("Invalid operation. Please enter a valid operation. (+, -, *, /): ")

        while True:
            try:
                number2 = float(input("Please enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "/":
            if number2 == 0:
                print("Error: Division by zero is not allowed. Please try again.")
                continue
            result = number1 / number2

        print(f"The result is {result:.2f}.")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    calculate()
