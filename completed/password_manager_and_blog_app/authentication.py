from user_model import User, Database
import blog_view
import tkinter
from components import Error, Fonts

canvas = tkinter.Tk()
canvas.geometry('600x400')
canvas.title('Blog Post')


heading = tkinter.StringVar(value='Login')  # Variable for header

isLogin = tkinter.BooleanVar(value=True)

# Variable for holding username
username = tkinter.StringVar(value='username')

# Variable for holding password
password = tkinter.StringVar(value='password')
confirm_password = tkinter.StringVar(value='confirm password')

switch_text = tkinter.StringVar(value='')


label = tkinter.Label(
    # Label for Showing Login or Sign up
    master=canvas, textvariable=heading, font=Fonts.heading())

textfield_username = tkinter.Entry(  # Username Input
    canvas, font=Fonts.custom(size=20), textvariable=username)

textfield_password = tkinter.Entry(  # Password Input
    canvas, font=Fonts.custom(size=20), textvariable=password)


confirm_password = tkinter.Entry(  # Password Input
    canvas, font=Fonts.custom(size=20), textvariable=confirm_password)

frame = tkinter.Frame(canvas)


def login():
    heading.set('Login')
    isLogin.set(True)
    label.pack(pady=10, expand=True)

    textfield_username.pack(pady=10, expand=True)
    textfield_password.pack(pady=10, expand=True)
    confirm_password.pack_forget()

    submit.grid_configure(column=0, row=0, sticky=tkinter.W+tkinter.E)
    switch.grid_configure(column=1, row=0,  sticky=tkinter.W+tkinter.E)
    switch_text.set(value="I don't have an account")


def createAccount():
    heading.set('Sign Up')
    isLogin.set(False)
    label.pack(pady=10, expand=True)

    textfield_username.pack(pady=10, expand=True)
    textfield_password.pack(pady=10, expand=True)
    confirm_password.pack(pady=10, expand=True)

    submit.grid_configure(column=0, row=0, sticky=tkinter.W+tkinter.E)
    switch.grid_configure(column=1, row=0,  sticky=tkinter.W+tkinter.E)
    switch_text.set(value="Already have an account")


def switcher():
    if isLogin.get():
        login()
    else:
        createAccount()


def make_switch():
    isLogin.set(value=not isLogin.get())
    switcher()  # Calling the switcher function after changing bool


def clear():
    user = textfield_username.get()
    label.pack_forget()
    textfield_password.pack_forget()
    textfield_username.pack_forget()
    confirm_password.pack_forget()
    frame.pack_forget()
    blog_view.Home(user, canvas)


def confirm():
    if isLogin.get():
        Database.authenticate(
            username=textfield_username.get(),
            password=textfield_password.get(),
            onComplete=clear
        )

    else:
        if textfield_username.get().strip() in Database.getUsernames():
            Error.userAlreadyExist()
        else:
            if textfield_password.get() == confirm_password.get():
                User.create_user(
                    username=textfield_username.get().strip(),
                    password=textfield_password.get(),
                    onComplete=clear
                )
            else:
                Error.passwordDontMatch()


switch = tkinter.Button(frame, pady=10, width=10,  # Button to switch between screens
                        textvariable=switch_text, font=Fonts.button(), command=make_switch)
submit = tkinter.Button(frame, pady=10, width=10,
                        text='Submit', font=Fonts.button(), command=confirm)


frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.pack(side='bottom', fill='x')


def runApp():
    try:
        with open('loggedin.txt', 'r') as loggedIn:
            user = loggedIn.read()
            if user in Database.getUsernames():
                blog_view.Home(user.strip(), canvas)
            else:
                raise Exception
    except:
        print(Exception)
        switcher()
    canvas.mainloop()
