"""..."""

# TODO: Create your MovieCollection class in this file
import csv
from operator import attrgetter
from movie import Movie


class MovieCollection:

    def __init__(self):
        movies = []
        super().__init__()
        self.movies = movies

    def __str__(self):
        for movie in self.movies:
            print(movie)
        return ""

    def add_movie(self, movie):
        self.movies.append(movie)

    def number_unwatched_movies(self):
        unwatched_movies = 0
        for movie in self.movies:
            if not movie.is_watched:
                unwatched_movies += 1
        return unwatched_movies

    def number_watched_movies(self):
        watched_movies = 0
        for movie in self.movies:
            if movie.is_watched:
                watched_movies += 1
        return watched_movies

    def load_movies(self, movies_file):
        in_file = open(movies_file, 'r')
        movies_read = csv.reader(in_file)
        movies_list = list(movies_read)
        for movie in movies_list:
            self.movies.append(
                Movie(title=movie[0], year=int(movie[1]), category=movie[2], is_watched="w" in movie[3]))

    def save_movies(self, movies_file):
        in_file = open(movies_file, 'w', newline="")
        movies_list = csv.writer(in_file)
        for movie in self.movies:
            movies_list.writerow([movie.title, movie.year, movie.category, "w" if movie.is_watched else "u"])

    def sort(self, key):
        self.movies.sort(key=attrgetter(key))
