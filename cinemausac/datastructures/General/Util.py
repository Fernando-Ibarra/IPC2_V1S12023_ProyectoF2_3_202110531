from ..user import LinkedUser, User, NodeUser
from ..theater import LinkedListTheater

ListaUsuarios: LinkedUser = LinkedUser()
ListaCines = LinkedListTheater()

user: User = User( "Fernando", "Ibarra", "49900123", "fi94457@gmail.com", "123456", "administrador")
nodeUser: NodeUser = NodeUser( user )
ListaUsuarios.push( nodeUser )