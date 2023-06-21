import datastructures.movieRoom as mr

class Theater(object):
    
    def __init__(self, name: str, rooms: mr.DoubleLinkedListMovieRoom) -> None:
        self.name = name
        self.rooms = rooms