user = {
    'usernamne': 'Jose',
    'access_level': 'admin'
}

# Decorator - must be a higher order function that takes in a function as argument, but it also must return a function as well    
def user_has_permissions(func):
    def secure_func():
        if user['access_level'] == 'admin':
            return func()
    return secure_func

my_function = lambda: 'Password is 1234'

my_secure_function = user_has_permissions(my_function)

print(my_secure_function())