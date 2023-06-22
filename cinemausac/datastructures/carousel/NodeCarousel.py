from . import Carousel

class NodeCarousel(object):
    
    __slost__ = 'carousel', 'prev', 'next'
    
    def __init__(self, carousel: Carousel, prev=None, next=None, ):
        self.carousel = carousel
        self.prev = prev
        self.next = next