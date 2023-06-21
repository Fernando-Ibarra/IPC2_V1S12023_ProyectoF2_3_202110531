from .Theater import Theater

class NodeTheater(object):
    
    __slost__ = 'theater', 'next'
    
    def __init__(self, theater: Theater, next=None, prev=None) -> None:
        self.theater = theater
        self.next = next