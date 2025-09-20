
from matplotlib import use
from blog_model import Post, Manager
import tkinter

from components import Entry, Fonts, Button, Label
from user_model import User


class Home:

    def __init__(self, user, root):
        # self.user = user
        # self.root = root

        navBar = tkinter.Frame()
        homePage = tkinter.Frame()
        create_view = tkinter.Frame(padx=20)
        post_view = tkinter.Frame(padx=20)
        navBar.columnconfigure(0, weight=1)
        navBar.columnconfigure(1, weight=1)
        navBar.columnconfigure(2, weight=1)
        navBar.columnconfigure(3, weight=1)
        navBar.pack(side='bottom', fill='x')

        # Track the current visible frame
        self.current_frame = None

        def clear():
            if self.current_frame is not None:
                self.current_frame.pack_forget()

        def show_home():
            clear()
            homePage.pack(side='top', anchor='w')
            self.current_frame = homePage

        def show_view_posts():
            clear()
            post_view.pack(side='top', anchor='center')
            self.current_frame = post_view

        def show_create_view():
            clear()
            create_view.pack(side='top', anchor='center')
            self.current_frame = create_view

        def logout():
            try:
                with open('loggedin.txt', 'w') as loggedIn:
                    loggedIn.write('')
                tkinter.BaseWidget.destroy(root)
            except:
                pass

        def getLatestContent():
            try:
                return Manager.get_user_post(user)[-1]['Content']
            except:
                return 'No Posts Yet'

        def getLatestTitle():
            try:
                return Manager.get_user_post(user)[-1]['Title']
            except:
                return 'No Title'

        Button('Home', navBar, 0, onPressed=show_home, type='grid')
        Button('Create Post', navBar, 1,
               onPressed=show_create_view, type='grid')
        Button('View My Post', navBar, 2,
               onPressed=show_view_posts, type='grid')
        Button('Log out', navBar, 3, color='red',
               textcolor='white', onPressed=logout, type='grid')

        Label(master=homePage, text=f'Welcome, {user.capitalize()}', pady=10,
              padx=10, side='top', anchor='w')

        Label(master=homePage, text='Your Previous Post', pady=10,
              padx=20, side='top', anchor='w', font=Fonts.custom(size=10))

        Label(master=homePage, text=f'Title: {getLatestTitle()}',
              padx=20, side='top', anchor='w', font=Fonts.custom(size=10, weight='bold'))
        Label(master=homePage, text=getLatestContent(), pady=5,
              padx=20, side='top', anchor='w', )

        # Only create CreateView widgets once
        CreateView(master=create_view, close=show_home)
        ViewPost(master=post_view)

        # Show home page by default
        show_home()


class CreateView:
    def __init__(self, master=tkinter.Frame, close=None):
        # title = tkinter.StringVar(value='')

        def create_post():
            title = heading.get()
            content = textbox.get(index1='1.0', index2=tkinter.END)

            Post.create(
                username=User.current_uid(),
                title=title,
                content=content
            )

            if close is not None:
                close()

        Label(master=master, text='Create Post', pady=10)

        # Button Section
        Button(master=master, text='Create', onPressed=create_post)

        # Title Section
        Label(master=master, text='Title:', pady=10,
              font=Fonts.small(), anchor='w')

        heading = Entry(master=master, anchor='w', )

        # Content Section
        Label(master=master, text='Content:', pady=10,
              font=Fonts.small(), anchor='w')
        textbox = tkinter.Text(master=master, font=Fonts.regular(), )
        textbox.pack()


class ViewPost:
    def __init__(self, master):
        # self.master = master
        Label(master=master, text='Your Posts', pady=10,)

        all_posts = Manager.get_user_post(User.current_uid())

        for post in all_posts:
            Label(master=master, text=f'Title: {post['Title']}', anchor='w')
            Label(master=master, text=f'Content: {post['Content']}')
