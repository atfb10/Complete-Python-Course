friend = 'rolf'
username = input('your name: ')

if friend == username: print('You Are Rolf')
else: print('imposter!')


username = input('Your name: ')
friends =[
    'jane',
    'jeff',
    'jose'
]

family =[
    'jan',
    'janice',
    'julia'
]

if username in friends:
    print('hi friend')
elif username in family:
    print('hello family')
else: print(f'who are you {username}?')

