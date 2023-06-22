from . import Category

class NodeCategory(object):
    
    __slost__ = 'category', 'prev', 'next'
    
    def __init__(self, category: Category, prev=None, next=None, ):
        self.category = category
        self.prev = prev
        self.next = next