"""
[1] add movie
[2] find movie
"""
movies = []


def menu():
    user_input = input("Enter 'a' to add\t'l' to see ur movies\t 'f' to find movies 'q' to quit program:")
    print()

    while user_input != 'q':

        if user_input == 'a':
            add_movies()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movies()
        else:
            print("unknown commands")
        user_input = input("\nEnter 'a' to add\t'l' to see ur movies\t 'f' to find movies 'q' to quit program:")


def add_movies():
    name = input("Enter movie name:")
    director = input("Enter Director name:")
    r_year = input("enter release year:")
    movie = {
        'name': name,
        'director': director,
        'year': r_year,
    }
    movies.append(movie)


def show_movies(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name:{movie['name']}")
    print(f"Director:{movie['director']}")
    print(f"Release year:{movie['year']}")
    print()


def find_movies():
    find_by=input("Enter which property by u want to find(name,director,year):")
    expected=input("enter what are u looking for")

    found_movies=find_by_attributes(movies, expected, lambda x: x[find_by])
    show_movies(found_movies)


def find_by_attributes(items, expected, finder):
    found=[]
    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found

menu()

