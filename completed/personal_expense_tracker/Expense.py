import datetime as dt

import json


class ExpenseModel:
    expenses = []

    def __init__(self, amount, name, description, date):
        self.amount = amount
        self.name = name
        self.description = description
        if date != '':
            self.date = date
        else:
            self.date = dt.datetime.now().date().strftime('%d/%m/%Y')

    def __to_dict__(self):
        return {
            "Amount": self.amount,
            "Name": self.name.lower(),
            "Description": self.description.lower(),
            "Date": self.date
        }


def convert_month_to_int(month):
    m = str(month).lower()
    if m == 'january':
        return '/01/'
    elif m == 'february':
        return '/02/'
    elif m == 'march':
        return '/03/'
    elif m == 'april':
        return '/04/'
    elif m == 'may':
        return '/05/'
    elif m == 'june':
        return '/06/'
    elif m == 'july':
        return '/07/'
    elif m == 'august':
        return '/08/'
    elif m == 'september':
        return '/09/'
    elif m == 'october':
        return '/10/'
    elif m == 'november':
        return '/11/'
    elif m == 'december':
        return '/12/'


def reduce(string):
    return str(string).lower().strip()


class ExpenseManager:
    expenses = []

    def __init__(self):
        with open('expenses.json', 'r') as f:
            self.expenses = json.load(f)

    def add_expense(self, expense):
        self.expenses.append(expense.__to_dict__())
        with open('expenses.json', 'w') as f:
            json.dump(self.expenses, f, indent=2)
        print("\nExpense Added Succefully\n".upper())

    def view_expenses(self):
        print("\nAll Expenses ::\n".upper())
        for expense in self.expenses:
            print('')
            print("Amount: ", expense['Amount'])
            print("Name: ", expense['Name'].capitalize())
            print("Description: ", expense['Description'].capitalize())
            print("Date: ", expense['Date'])
            print('')

    def delete_expense(self, name):
        for expense in self.expenses:
            if name.lower() in expense['Name'].lower():
                index = self.expenses.index(expense)
                self.expenses.pop(index)
                with open('expenses.json', 'w') as f:
                    json.dump(self.expenses, f, indent=2)
                print("\nDeleted Successfully\n".upper())

    def get_total_by_month(self, month: str | None = None):
        expenses_total = 0
        if month != None:
            get_month = convert_month_to_int(month)
            for expense in self.expenses:
                if get_month in expense['Date']:
                    expenses_total = expenses_total + expense['Amount']
            if expenses_total == 0:
                return f'No Expenses for {month}'
            return expenses_total
        else:
            for expense in self.expenses:
                expenses_total = expenses_total + expense['Amount']
            return expenses_total

    def get_total_by_name(self, name: str | None = None):
        expenses_total = 0
        if name != None:
            for expense in self.expenses:
                if reduce(name) in reduce(expense['Name'].lower()):
                    expenses_total = expenses_total + expense['Amount']
            if expenses_total == 0:
                return f'No Expenses for {name}'
            return expenses_total
        else:
            for expense in self.expenses:
                expenses_total = expenses_total + expense['Amount']
            return expenses_total

    def get_all_names(self):

        names = []

        with open('expenses.json', 'r') as expenses_file:
            file = json.load(expenses_file)

            for expense in file:
                names.append(expense['Name'])

        return names

    def get_all_prices(self):

        names = []

        with open('expenses.json', 'r') as expenses_file:
            file = json.load(expenses_file)

            for expense in file:
                # if expense['Amount'] > :
                names.append((expense['Amount']))
                # else:
                #     names.append(0)

        return names


def get_amount_spent():
    try:
        choice = int(input('Enter Amount Spent: '))
        return choice
    except ValueError:
        while True:
            try:
                choice = int(input('Enter valid amount, e.g - 1000: '))
                return choice
            except ValueError:
                continue
