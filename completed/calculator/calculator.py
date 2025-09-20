import tkinter as tk

from fonts import fonts


canvas = tk.Tk()
canvas.title('Calculator')
canvas.geometry('400x600')
canvas.config(background='white')

# Frames
frame = tk.Frame(canvas)

# Tkinter Variable
display_value = tk.StringVar(master=frame, value='0')
error_value = tk.StringVar(master=frame, value='')
result_value = tk.StringVar(master=frame, value='')
currentOperator = tk.StringVar(master=frame, value='')
previousOperator = tk.StringVar(master=frame, value='')

# Tkinter Classes
display = tk.Label(master=frame, width=10, font=fonts.regular(),
                   textvariable=display_value, state='active', anchor='e', activebackground='white', padx=10,)
error = tk.Label(master=frame, width=10, font=fonts.error(),
                 textvariable=error_value, state='active', anchor='e', activebackground='white', padx=10,)
result = tk.Label(master=frame, font=fonts.result(),
                  textvariable=result_value, state='active', anchor='e', padx=10, activebackground='white', activeforeground='grey')


frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.config(background='white')
frame.pack(fill='x', side='bottom')


def parse(x):
    try:
        if float(x).is_integer():
            return int(x)
        else:
            return round(float(x), ndigits=7)
    except:
        return str(x)


def reset():
    display_value.initialize('0')
    result_value.initialize('')
    currentOperator.initialize('')


class Button:
    total = parse(0)
    multDivTotal = parse(1)

    def __init__(self, column, row, text, columnspan=1, width=10, isOperator=False, isEqualTo=False, color='lightgrey'):
        self.column = column
        self.row = row
        self.text = text
        self.columnspan = columnspan
        self.width = width
        self.isOperator = isOperator
        self.isEqualTo = isEqualTo

        button = tk.Button(master=frame)
        if isOperator:
            button.config(text=text, height=3, width=width, foreground='white',
                          font=fonts.button(), background='lightblue')
        else:
            button.config(text=text, height=3, width=width,
                          font=fonts.button(), background=color)
        button.grid(column=column, row=row, columnspan=columnspan,
                    sticky=tk.W+tk.E,)

        def get_value():
            # Current value

            error.grid_remove()
            error_value.initialize('')
            previous = display_value.get()

            # Handle Sign Change
            if text == '+/-':
                if error_value.get() != '':
                    pass
                else:
                    if previous.startswith('0'):
                        pass
                    else:
                        if previous[0] == '-':
                            display_value.set(previous.strip('-'))
                        else:
                            display_value.set(f'-{previous.strip()}')

            # Handle Clear
            elif text == 'AC':
                reset()
            # Handle backspace
            elif text == '←':
                if error_value.get() != '':
                    pass
                else:
                    if previous.startswith('0') and '.' not in previous:
                        pass
                    else:
                        if len(previous) > 1:
                            display_value.set(
                                previous.removesuffix(previous[-1]))
                        else:
                            display_value.set('0')

            # Handle Decimal
            elif text == '.':
                if error_value.get() != '':
                    pass
                else:
                    if previous.endswith('.'):
                        new = previous.removesuffix('.')
                        display_value.set(new)
                    elif '.' not in previous:
                        display_value.set(f'{previous}.')
                    else:
                        pass

            # Handle Operation
            elif text == '+' or text == '-' or text == '÷' or text == '×' or text == '=':
                # if previousOperator.get() == text and result_value.get().strip() == display_value.get().strip():
                #     currentOperator.set(text)
                # else:
                if error_value.get() != '':
                    pass
                else:
                    result.grid_configure(
                        column=0, row=0, columnspan=4, sticky='we', pady=20)
                    currentOperator.set(text)

                    self.do_math()

            # Handle Entries
            elif previous == '0':
                display_value.set(text)
            elif currentOperator.get() != '':
                display_value.set(text)
                currentOperator.initialize('')
            else:
                display_value.set(f'{previous}{text}')
            return self.text
        button.config(command=get_value)

    # def handle_equal(self):

    # Calculator Logic
    def do_math(self):

        # Addition
        if currentOperator.get() == '+':
            self.equalize()
            if previousOperator.get().strip() == '=':
                previousOperator.set(currentOperator.get())
                result_value.set(display_value.get())
            else:
                previousOperator.set(currentOperator.get())
                self.total = parse(self.total) + parse(display_value.get())
                result_value.set(f'{self.total}'.strip())

        # Subtraction
        elif currentOperator.get() == '-':
            self.equalize()
            if previousOperator.get().strip() == '=':
                previousOperator.set(currentOperator.get())
                result_value.set(display_value.get())
            elif result_value.get() == '':
                previousOperator.set(currentOperator.get())
                result_value.set(f'{display_value.get()}'.strip())
            else:
                previousOperator.set(currentOperator.get())
                self.total = parse(self.total) - parse(display_value.get())
                result_value.set(f'{self.total}'.strip())

        # Multiplication
        elif currentOperator.get() == '×':
            self.equalize()
            if previousOperator.get().strip() == '=':
                previousOperator.set(currentOperator.get())
                result_value.set(display_value.get())
            elif result_value.get() == '':
                self.equalize()
                previousOperator.set(currentOperator.get())
                result_value.set(f'{display_value.get()}'.strip())
            else:
                previousOperator.set(currentOperator.get())
                self.multDivTotal = parse(
                    self.multDivTotal) * parse(display_value.get())
                result_value.set(f'{self.multDivTotal}'.strip())
        # Division
        elif currentOperator.get() == '÷':
            self.equalize()
            if previousOperator.get().strip() == '=':
                previousOperator.set(currentOperator.get())
                result_value.set(display_value.get())
            elif result_value.get() == '':
                previousOperator.set(currentOperator.get())
                result_value.set(f'{display_value.get()}'.strip())
            else:
                previousOperator.set(currentOperator.get())
                try:
                    self.total = parse(
                        self.total) / parse(display_value.get())
                except ZeroDivisionError:
                    error_value.set('Cannot Divide By Zero')
                    error.grid_configure(
                        column=0, row=1, columnspan=4, sticky='we', pady=20,)
                    reset()

                result_value.set(f'{self.total}'.strip())

        # Equal to
        else:
            self.equalize(keepResult=False)

    # Handle Equal Sign
    def equalize(self, keepResult=True):
        def __base__(x):
            previousOperator.set('=')
            display_value.set(str(parse(x)))
            result_value.set(x)

        # Addition
        if previousOperator.get() == '+':
            final = parse(result_value.get()) + parse(display_value.get())
            __base__(final)

        # Subtraction
        if previousOperator.get() == '-':
            final = parse(result_value.get()) - parse(display_value.get())
            __base__(final)

        # Multiplication
        if previousOperator.get() == '×':
            final = parse(result_value.get()) * parse(display_value.get())
            __base__(final)

        # Division
        if previousOperator.get() == '÷':
            try:
                final = parse(
                    result_value.get()) / parse(display_value.get())
                __base__(final)
            except ZeroDivisionError:
                error_value.set('Cannot Divide By Zero')
                error.grid_configure(
                    column=0, row=1, columnspan=4, sticky='we', pady=20,)
                display_value.initialize('0')
                result_value.initialize('')
                currentOperator.initialize('')

        if keepResult:
            pass
        else:
            result.grid_remove()


def main():
    # Calculator Display
    display.grid_configure(column=0, row=1, columnspan=4, sticky='we', pady=20)

    # Display Buttons
    for row in range(5):
        for column in range(4):
            if row == 0:
                Button(text=column+1, row=row+2, column=column)
                if column == 3:
                    Button(text="÷", column=column, row=row+2, isOperator=True)
            elif row == 1:
                Button(text=column+4, row=row+2, column=column)
                if column == 3:
                    Button(text="×", column=column, row=row+2, isOperator=True)
            elif row == 2:
                Button(text=column+7, row=row+2, column=column)
                if column == 3:
                    Button(text="+", column=column, row=row+2, isOperator=True)
            elif row == 3:
                Button(text=0, column=column, row=row+2)
                if column == 0:
                    Button(text='+/-', row=row+2, column=column,)
                if column == 2:
                    Button(text='AC', row=row+2, column=column,)
                if column == 3:
                    Button(text='-', row=row+2, column=column, isOperator=True)

    Button(text='.', row=6, column=0,)
    Button(text='←', row=6, column=1,  color='orange')
    Button(text='=', row=6, column=2, columnspan=2, width=20, color='lightblue')


main()
canvas.mainloop()
