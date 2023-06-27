class FavMovie(object):
    
    def __init__(self, name: str, lastName: str, title: str, director: str, year: str, date: str, time: str, image: str, price: int ) -> None:
        self.name = name
        self.lastName = lastName
        self.title: str = title
        self.director: str = director
        self.year: str = year
        self.date: str = date
        self.time: str = time
        self.image: str = image
        self.price: int = price