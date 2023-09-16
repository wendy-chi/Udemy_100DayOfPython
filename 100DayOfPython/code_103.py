import operation as operation


def calculation(number1, input_operation, number2):
    if input_operation == "+":
        return int(number1) + int(number2)
    elif input_operation == "-":
        return int(number1) - int(number2)
    elif input_operation == "*":
        return int(number1) * int(number2)
    else:
        return int(number1) / int(number2)


def start_new_cal():
    first_number = input("What is your first number?")

    print("\n+\n-\n*\n\\")

    operation = input("Pick an operation.")
    second_number = input("what is your second number?")
    print(calculation(first_number, operation, second_number))
    return True


start_cal = True

start_new_cal()

while start_cal:
    continue_cal = input(f"Type 'y' to continue calculating with {calculation(first_number, operation, second_number)}"
                         f", or type 'n' to start a new calculation:")
    if continue_cal == 'y':
        start_cal = False
        first_number = calculation(calculation(number1, input_operation, number2))
        calculation(first_number, operation, second_number)
    else:
        start_new_cal()


