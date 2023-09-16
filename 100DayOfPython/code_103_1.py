def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    num1 = float(input("what is the first number?"))
    num2 = float(input("what is the second number?"))

    for symbol in operations:
        print(symbol)

    continue_cal = True
    while continue_cal:
        operation_symbol = input("Pick an operation:")
        calculator_function = operations[operation_symbol]
        first_answer = calculator_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        selection = input(f"Type 'y' to continue calculating with {first_answer}, "
                          f"or type 'n' to start a new calculator.:")
        if selection == "y":
            num1 = first_answer
            num2 = float(input("what is the next number?"))
        else:
            continue_cal = False
            calculator()


calculator()



