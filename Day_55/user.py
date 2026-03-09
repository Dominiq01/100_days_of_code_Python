class User():
    def __init__(self,username):
        self.username = username
        self.is_logged_in = False

def is_authenticated_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            func(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.username}'s blog post")

new_user = User(username="Dominik")
new_user.is_logged_in = False
create_blog_post(new_user)