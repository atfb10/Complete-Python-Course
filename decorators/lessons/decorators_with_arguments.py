import functools as ft

user = {
    'id': 1,
    'username': 'aforestier10',
    'access_level': 'admin'
}

def permission_by_access_level(access_level):
    def user_has_permissions(func):
        @ft.wraps(func)
        def wrapper(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                raise PermissionError('Not correct access level')
        return wrapper
    return user_has_permissions

@permission_by_access_level('admin')
def square(number: int):
    return f'{number} squared = {str(number ** 2)}'

@permission_by_access_level('admin')
def print_password():
    print('The password is 1234')

print(square(3))
print_password()