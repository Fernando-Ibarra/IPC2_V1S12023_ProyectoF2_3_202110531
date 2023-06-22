import datastructures.movie as m

class Category(object):
    def __init__(self, name: str, movies: m.LinkedListMovie ) -> None:
        self.name = name
        self.movies = movies