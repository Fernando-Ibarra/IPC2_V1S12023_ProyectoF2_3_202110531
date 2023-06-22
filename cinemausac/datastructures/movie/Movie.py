class Movie(object):
    
    def __init__(self, title: str, director: str, year: str, date: str, time: str, image: str, price: int ) -> None:
        self.title: str = title
        self.director: str = director
        self.year: str = year
        self.date: str = date
        self.time: str = time
        self.image: str = image
        self.price: int = price