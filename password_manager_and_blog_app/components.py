
import tkinter
import tkinter.messagebox
from typing import Literal  # import messagebox, Button, Label, W, E


class Fonts:
    @classmethod
    def heading(cls):
        return ('poppins', 40, 'bold')

    @classmethod
    def regular(cls):
        return ('poppins', 15, 'normal')

    @classmethod
    def button(cls):
        return ('poor richard', 13, 'bold')

    @classmethod
    def small(cls):
        return ('poppins', 10, 'normal')

    @classmethod
    def custom(cls, size, weight='normal'):
        return ('poppins', size, weight)


class Error:
    @staticmethod
    def passwordDontMatch():
        return tkinter.messagebox.showerror(
            title='Password Error',
            message='Passwords do not match\nPlease check passwords and try again'
        )

    @staticmethod
    def passwordIncorrect():
        return tkinter.messagebox.showerror(
            title='Password Error',
            message='Passwords Incorrect'
        )

    @staticmethod
    def userNotFound():
        return tkinter.messagebox.showerror(
            title='User Error',
            message='User not found'
        )

    @staticmethod
    def userAlreadyExist():
        return tkinter.messagebox.showerror(
            title='User Error',
            message='Username Already exist'
        )

    @staticmethod
    def userDoesNotExist():
        return tkinter.messagebox.showerror(
            title='User Error',
            message='Username Already exist'
        )

    @staticmethod
    def deleteConfirmation():
        return tkinter.messagebox.showerror(
            icon='warning',
            title='Confirmation',
            message='Are you sure?\nAction is irreversible',
            default='Yes'
        )


class Button():

    def __init__(self, text='', master=None, column=0, color='white', textcolor='black', onPressed=None, type: Literal['pack', 'grid'] = 'pack'):
        self = tkinter.Button(
            master=master,
            width=10,
            text=text,
            borderwidth=1,
            font=Fonts.button(),
            background=color,
            foreground=textcolor,
            command=onPressed,
        )
        if type == 'grid':
            self.grid_configure(column=column, row=0,
                                sticky=tkinter.W+tkinter.E)
        elif type == 'pack':
            self.pack(side='top', anchor='e')


class Label():

    def __init__(self, master=None, text='', padx=0, pady=0, anchor='center', side='top', font=Fonts.regular(), ):

        self = tkinter.Label(
            master=master,
            text=text,
            font=font,
            padx=padx,
            pady=pady,
        )
        self.pack(side=side, anchor=anchor, in_=master)


class Entry():

    def __init__(self, master=None, anchor='center', font=Fonts.custom(size=17), ):

        self.textvariable = tkinter.StringVar()

        entry = tkinter.Entry(
            master=master,
            # text='text',
            width=40,
            font=font,
            textvariable=self.textvariable
        )
        entry.pack(anchor=anchor)

    def get(self):
        return self.textvariable.get()
