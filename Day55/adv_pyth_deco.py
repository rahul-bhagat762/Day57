class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False
def is_authenticated_decorater(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorater
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User('Ram')
new_user.is_logged_in = True
create_blog_post(new_user)