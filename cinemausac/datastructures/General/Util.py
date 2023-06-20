from ..user import LinkedUser, User, NodeUser

ListaUsuarios: LinkedUser = LinkedUser()

user: User = User( "Fernando", "Ibarra", "49900123", "fi94457@gmail.com", "123456", "administrador")
nodeUser: NodeUser = NodeUser( user )
ListaUsuarios.push( nodeUser )