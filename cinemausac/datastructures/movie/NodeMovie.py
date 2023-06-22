from . import Movie

class NodeMovie(object):
    
    __slost__ = 'movie', 'next'
    
    def __init__(self, movie: Movie, next = None ) -> None:
        self.movie = movie
        self.next = next