from .CreditCard import CreditCard

class NodeCreditCard(object):
    
    __slots__ = 'creditcard', 'next', 'prev'
    
    def __init__(self, creditcard: CreditCard, prev=None, next=None, ) -> None:
        self.creditcard = creditcard
        self.prev = prev
        self.next = next