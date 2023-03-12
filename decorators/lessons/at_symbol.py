import functools

my_user = {'id': 1, 'username': 'aforestier10', 'access_level': 'admin'}

def user_has_permissions(func):
    @functools.wraps(func)
    def wrapper():
        if my_user['access_level'] == 'admin':
            return func()
        else:
            raise PermissionError('Must be admin')
    return wrapper

@user_has_permissions
def silly_function():
    return 'Password: silly1234'

# Prints Password: silly1234
print(silly_function())
print(silly_function.__name__)