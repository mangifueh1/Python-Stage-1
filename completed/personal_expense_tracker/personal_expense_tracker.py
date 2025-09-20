
from Expense import ExpenseModel, ExpenseManager, get_amount_spent

import matplotlib.pyplot as plt

# names = ['house', 'car', 'school', 'work', 'play']

# prices = [13, 12, 143, 132, 132]


def __main__():
    while True:

        print('Main Menu')
        print('1. Add Expense\n2. View All Expenses\n3. Get Total Expenditure\n4. Get Total by Month\n5. Get Total By Name\n6. Delete Expense\n7. View Expense Chart\n8. Exit')
        try:
            choice = int(input('Pick an Option: '))
        except ValueError:
            print("\nPlease Pick a valid number\n".upper())
            continue

        if choice == 1:
            amount = get_amount_spent()
            name = input('Name: ')
            description = input('Description: ')
            date = input('Date: e.g - dd/mm/yyyy ')
            manager.add_expense(ExpenseModel(amount, name, description, date))
            continue

        elif choice == 2:
            manager.view_expenses()
            continue

        elif choice == 3:
            print(f'\nTotal Expediture: {manager.get_total_by_month()}\n')
            continue

        elif choice == 4:
            month = input('\nEnter the month, e.g - January: ')
            print(
                f'\nTotal Expediture for {month.capitalize()}: {manager.get_total_by_month(month)}\n')
            continue

        elif choice == 5:
            name = input('\nEnter the name, e.g - House: ')
            print(
                f'\nTotal for {name}: {manager.get_total_by_name(name)}\n')
            continue

        elif choice == 6:
            name = input('\nEnter the name, e.g - House: ')
            manager.delete_expense(name)

        elif choice == 7:
            names = manager.get_all_names()
            prices = manager.get_all_prices()

            plt.plot(names, prices)
            plt.show()

        elif choice == 8:
            print('\nPROGRAM IS CLOSING\n')
            break

        else:
            print('\nPlease Choose a Valid Option\n'.upper())


manager = ExpenseManager()

__main__()
