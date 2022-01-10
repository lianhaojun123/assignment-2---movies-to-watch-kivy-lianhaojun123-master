"""..."""


# TODO: Create your Movie class in this file


class Movie:

    def __init__(self, title="", year=0, category="", is_watched=False):

        self.is_watched = is_watched
        self.year = year
        self.category = category
        self.title = title

    def __str__(self):
        return "{} - {} ({}) ({})".format(self.title, self.year, self.category, self.movie_watch_check())

    def movie_watch_check(self):
        if self.is_watched:
            return "watched"
        else:
            return "unwatch"
