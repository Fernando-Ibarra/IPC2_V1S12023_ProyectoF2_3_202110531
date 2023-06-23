class CreditCard(object):
        
    def __init__(self, type: str, number: str, owner: str, expiredTime: str) -> None:
        self.type = type
        self.number = number
        self.owner = owner
        self.expiredTime = expiredTime