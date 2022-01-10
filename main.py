"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# TODO: Create your main program in this file, using the MoviesToWatchApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection


class MoviesToWatchApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()

    def build(self):
        self.title = "Movies to Watch 2.0"
        self.root = Builder.load_file("app.kv")
        self.display_movies()
        return self.root

    def display_movies(self):
        self.movie_collection.load_movies("movies.csv")
        self.display_watched_unwatched_movies()
        for movie in self.movie_collection.movies:
            if movie.is_watched:
                movie_button = Button(text="{} ({} from {}) watched".format(movie.title, movie.category, movie.year))
                movie_button.background_color = (51, 102, 0, 0.2)
            else:
                movie_button = Button(text="{} ({} from {})".format(movie.title, movie.category, movie.year))
                movie_button.background_color = (0, 102, 153, 0.2)
            self.root.ids.display_box.add_widget(movie_button)

    def display_watched_unwatched_movies(self):
        self.root.ids.display_watched_unwatch.text = "To watch: " + str(self.movie_collection.number_unwatched_movies()) \
                                                     + "Watched: " + str(self.movie_collection.number_watched_movies())



    def clear_input_information(self):
        self.root.ids.title_input.text = ""
        self.root.ids.category_input.text = ""
        self.root.ids.year_input.text = ""


if __name__ == '__main__':
    MoviesToWatchApp().run()
