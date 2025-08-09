print('Calculator Program')

print('\n" + " For Addition \n" - " For Subtraction \n" * " For Multiplication \n" / " For Division')


def operation(operator):
    numbers = input("\nEnter numbers then press enter: ")
    total = int(numbers)

    while True:
        print(f'result: {total}')
        numbers = input("\nEnter next number: ")
        if numbers.isdigit():
            if str(operator).strip() == "+":
                total = total + int(numbers)
            if str(operator).strip() == "-":
                total = total - int(numbers)
            if str(operator).strip() == "/":
                try:
                    total = total / int(numbers)
                except ZeroDivisionError:
                    numbers = print("You can't divide by zero. Try again: ")
            if str(operator).strip() == "*":
                total = total * int(numbers)
        else:
            print(f'\nThe answer is {total}')
            break


def calculator():
    while True:
        operator = input('\nSelect operator: '.upper()).strip()
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            operation(operator)
        else:
            print('\nError: Please select a valid operator and try again')
            break


calculator()
