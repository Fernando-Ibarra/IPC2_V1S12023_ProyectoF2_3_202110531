from .MovieRoom import MovieRoom

class NodeMovieRoom(object):
    
    __slots__ = 'movieRoom', 'next', 'prev'
    
    def __init__(self, movieRoom: MovieRoom, prev=None, next=None, ) -> None:
        self.movieRoom = movieRoom
        self.prev = prev
        self.next = next