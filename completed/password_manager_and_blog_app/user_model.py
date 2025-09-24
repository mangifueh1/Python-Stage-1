from components import Error
import hashlib
import json

db = 'password_manager_and_blog_app/users.json'


def newlinePrint(x):
    print(f'{x}\n')


# def getUsers():


class User:
    users = []
    # def __init__(self, username=str, password=str):

    @classmethod
    def create_user(cls, username=str, password=str, onComplete=None, *args, **kwargs):
        cls.users = Database.getUsers()
        # Hashing Password
        algorithm = hashlib.sha256(password.encode())
        hashed_password = algorithm.hexdigest()

        # Organizing Information
        userSchema = {
            'Username': username.lower(),
            'Password': hashed_password
        }

        if username in Database.getUsernames():
            print()
            newlinePrint('Username already exist')
        else:
            # Adding Info to list
            cls.users.append(userSchema)
            newlinePrint('*Account Created*')
            if onComplete is not None:
                # Call the passed function
                onComplete(*args, *kwargs)
                print()
                print('Successful')
            else:
                print("No function passed.")

        # Writing to database
        Database.saveUsers(cls.users)

    @classmethod
    def delete_user(cls, username=str):
        userList = cls.users = Database.getUsers()

        for user in userList:
            # print(user['Username'])
            if username.lower() == user['Username']:
                # print(user)
                userList.remove(user)
            else:
                pass
        Database.saveUsers(userList)

    @staticmethod
    def current_uid():

        with open('loggedin.txt', 'r') as userFile:
            username = userFile.read()
            return username.strip()


class Database:

    @classmethod
    def currentUser(cls):
        return

    # Method for getting users from JSON file
    @classmethod
    def getUsers(cls):
        # Open and read the database
        try:
            with open(db, 'r') as userFile:
                return list(json.load(userFile))
        except json.decoder.JSONDecodeError:
            return []

    # Method to get only usernames
    @classmethod
    def getUsernames(cls, newData=list):
        # Open and read the database
        try:
            with open(db, 'r') as userFile:
                userList = list(json.load(userFile))
                usernames = []

                for user in userList:
                    usernames.append(user['Username'])

                return usernames
        except json.decoder.JSONDecodeError:
            return []

    # Method to write changes to JSON file
    @classmethod
    def saveUsers(cls, newData=list):
        # Open and read the database
        try:
            with open(db, 'w') as userFile:
                json.dump(newData, fp=userFile, indent=4)
        except:
            print("\n An Error Occured When writing to db")

    @classmethod
    def authenticate(cls, username=str, password=str, onComplete=None, *args, **kwargs,):

        with open(db, 'r') as userFile:
            users = list(json.load(userFile))
            algorithm = hashlib.sha256(password.encode())
            hashed_password = algorithm.hexdigest()

            if username not in Database.getUsernames():
                Error.userDoesNotExist()
            else:
                for user in users:
                    if user['Username'] == username.lower() and user['Password'] == hashed_password:
                        print('')
                        newlinePrint(f'Welcome Back, {username}')

                        if onComplete is not None:
                            # Call the passed function
                            onComplete(*args, *kwargs)
                            with open('loggedin.txt', 'w') as loggedIn:
                                loggedIn.write(username)
                        else:
                            print("No function passed.")

                    elif user['Username'] == username and user['Password'] != hashed_password:
                        Error.passwordIncorrect()

                    elif user['Username'] != username:
                        pass
