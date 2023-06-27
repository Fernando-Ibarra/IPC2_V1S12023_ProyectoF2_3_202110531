from ..user import LinkedUser, User, NodeUser
from ..theater import LinkedListTheater
from ..category import CircularlyLinkedListCategory
from ..carousel import CircularlyLinkedListCarousel
from ..creditCard import DoubleLinkedListCreditCard

ListaUsuarios: LinkedUser = LinkedUser()
ListaCines: LinkedListTheater = LinkedListTheater()
ListaTarjetas: DoubleLinkedListCreditCard = DoubleLinkedListCreditCard()
ListaCategoria: CircularlyLinkedListCategory = CircularlyLinkedListCategory()
ListaPeliculas: CircularlyLinkedListCarousel = CircularlyLinkedListCarousel()
ListaFavMovie = []
ListaTickets = []

user: User = User( "Fernando", "Ibarra", "49900123", "fi94457@gmail.com", "123456", "administrador")
nodeUser: NodeUser = NodeUser( user )
ListaUsuarios.push( nodeUser )