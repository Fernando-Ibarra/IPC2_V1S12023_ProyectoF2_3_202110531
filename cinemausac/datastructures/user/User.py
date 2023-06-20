class User(object):
    def __init__(self, name: str, lastName: str, phoneNUmber: str, email: str, password: str, rol: str) -> None:
        self.rol = rol
        self.name = name
        self.lastName = lastName
        self.phoneNUmber = phoneNUmber
        self.email = email
        self.password = password