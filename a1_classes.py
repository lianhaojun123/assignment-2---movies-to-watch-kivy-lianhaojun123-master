"""..."""
# TODO: Copy your first assignment to this file, then update it to use Movie class
# Optionally, you may also use MovieCollection class

from movie import Movie
from moviecollection import MovieCollection


def main():
    movie_collection = MovieCollection()
    movie_collection.load_movies("movies.csv")
    print(f'''Movies To Watch 2.0 - by Haojun Lian
{len(movie_collection.movies)} movies loaded''')
    get_menu()
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "L":
            print_movies_list(movie_collection)
            get_menu()
            choice = input("Enter your choice: ").upper()
        elif choice == "A":
            add_movies(movie_collection)
            get_menu()
            choice = input("Enter your choice: ").upper()
        elif choice == "W":
            get_watches_movies(movie_collection)
            get_menu()
            choice = input("Enter your choice: ").upper()
        else:
            print("Invalid Menu Choice")
            choice = input("Enter your choice: ").upper()
    if choice == "Q":
        movie_collection.save_movies("movies.csv")
        print(f'''{len(movie_collection.movies)} movies saved to movies.csv
Have a nice day :)''')


def get_menu():
    # output the menu
    print('''Menu:
L - List movies
A - Add new movie
W - Watch a movie
Q - Quit''')


def print_movies_list(movie_collection):
    movie_collection.sort("year")
    for i, movie in enumerate(movie_collection.movies):
        if movie.is_watched:
            print("{}. * {:35} - {:4} ({})".format(i, movie.title, movie.year, movie.category))
        else:
            print("{}.   {:35} - {:4} ({})".format(i, movie.title, movie.year, movie.category))
    print("{} Movies watched {} Movies unwatched".format(movie_collection.number_watched_movies(),
                                                         movie_collection.number_unwatched_movies()))


def check_all_movies_watched(movie_collection):
    for movie in movie_collection.movies:
        if not movie.is_watched:
            return False
    else:
        return True


def get_watches_movies(movie_collection):
    if check_all_movies_watched(movie_collection):
        print("No more movies to watch")
    else:
        movie_num_check_input = False
        print("Enter the number of a movie to mark as watched")
        while not movie_num_check_input:
            try:
                movie_number = int(input(">>>"))
                if movie_number < 0:
                    print("Number must be >= 0")
                elif movie_number > len(movie_collection.movies):
                    print("Invalid movie number")
                else:
                    movie_num_check_input = True
            except ValueError:
                print("Invalid input; enter a valid number")
        movie = movie_collection.movies[movie_number]
        if movie.is_watched:
            print(f"You have already watched {movie.title}")
        else:
            movie.is_watched = True
            print("{} from {} watched".format(movie.title, movie.year))


def add_movies(movie_collection):
    title = input("Title:")
    while title == "":
        print("Input can not be blank")
        title = input("Title:")
    movie_year_check = False
    while not movie_year_check:
        try:
            year = int(input("Year:"))
            if year < 0:
                print("Number must be >= 0")
            else:
                movie_year_check = True
        except ValueError:
            print("Invalid input; enter a valid number")
    category = input("Category:")
    while category == "" or category not in (
            "Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"):
        print("Invalid category.Please try again! ")
        category = input("Category:")
    print("{}-{} from {} added to movie list".format(title, year, category))
    movie_collection.add_movie(Movie(title, year, category, is_watched=False))


main()
