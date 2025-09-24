
import json


blogDB = 'password_manager_and_blog_app/posts.json'


class Post:
    posts = []

    @classmethod
    def create(cls, username, title, content):
        posts = cls.posts = Manager.get_all_post()

        schema = {
            'User': f'{username}',
            'Title': f'{title}',
            'Content': f'{content}'
        }

        posts.append(schema)

        Manager.save(posts)

    # @classmethod
    # def delete(cls, username, title):
    #     posts = cls.posts = Manager.get_user_post()

    #     for post in posts:
    #         # checks if post belongs to user
    #         if title == post['Title']:
    #             posts.remove(post)

    #         elif title != post['Title']:
    #             pass

    #     Manager.save(posts)


class Manager:
    # Method for getting users from JSON file
    @classmethod
    def get_all_post(cls):
        # Open and read the database
        try:
            with open(blogDB, 'r') as userFile:
                post_list = list(json.load(userFile))

                return post_list
        except json.decoder.JSONDecodeError:
            return []
        except FileNotFoundError:
            return []

    @classmethod
    def get_user_post(cls, username):
        # Open and read the database
        try:
            with open(blogDB, 'r') as userFile:
                post_list = list(json.load(userFile))
                user_posts = []
                for post in post_list:
                    if username == post['User']:  # Get Only the users posts
                        user_posts.append(post)
                return user_posts
        except json.decoder.JSONDecodeError:
            return []
        except FileNotFoundError:
            return []

    # Method to write changes to JSON file
    @classmethod
    def save(cls, newData=list):
        # Open and read the database
        try:
            with open(blogDB, 'w') as userFile:
                json.dump(newData, fp=userFile, indent=4)
        except:
            print("\n An Error Occured When writing to db")
