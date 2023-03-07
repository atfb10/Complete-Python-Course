def greet() -> None:
    print('Hello')
    return

def multiply(x, y) -> int:
    print(f'{x} * {y} = {x*y}')
    return x * y

def before_and_after(func):
    print("Before...")
    func()
    print("After.")
    return

before_and_after(greet)
before_and_after(lambda: multiply(12, 921))
print('\n\n\n')

movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "The Irishman", "director": "Scorsese"},
    {"name": "Klaus", "director": "Pablos"},
    {"name": "1917", "director": "Mendes"},
]

# function that finds a movie by using an argument that is a function returning the correct movie
def find_movie(search, movie_list, finder_func):
    movie_found = False
    for movie in movie_list:
        if finder_func(movie) == search:
            movie_found = True
            movie_name = movie['name']
            movie_director = movie['director']
            print('Your Search Yielded this Result: ')
            print(f'{movie_name} directed by {movie_director}')
    if not movie_found:
        print('Your search yielded 0 results')
    return

# Get user data
find_by = input('Enter \'name\' or \'director\' ')
looking_for = input('Search: ')

# Call find movie.
# If the user searches something valid. It prints the name and director.
# If the user searches something not in the list, it prints "Search yielded 0 results"
find_movie(looking_for, movies, lambda movie: movie[find_by])