import xml.etree.ElementTree as ET
from xml.dom import minidom

from . import Carousel, NodeCarousel

class CircularlyLinkedListCarousel(object):

    def __init__(self) -> None:
        """ Create an empty list """
        self.head: NodeCarousel = None
        self.size = 0
        
    def __len__( self ):
        """ Return size methods
        
        Returns:
            [ int ] - The number of elements in the stack
        
        """
        return self.size
    
    def totalLen(self):
        return len(self)
        
    def isEmpty(self) -> bool:
        """ Validate Empty stack
        
        Returns:
            [ boolean ] - Return True if the stack is empty
        
        """
        return self.head == None

    def push(self, carousel: Carousel):
        """push - Add a Category to the back of the list

        Args:
            category (Category): category object
        """
        tempNode: NodeCarousel = NodeCarousel( carousel )

        if self.head is None:
            tempNode.next = tempNode
            tempNode.prev = tempNode
            self.head = tempNode
            self.size += 1
            return None
        else:
            ultimo: NodeCarousel = self.head.prev

            tempNode.next = self.head
            tempNode.prev = ultimo

            self.head.prev = tempNode
            ultimo.next = tempNode
            self.size += 1
            return None
            
    def modify( self, indexCome: int, field: str, value ) -> None:
        index: int = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            auxNode: NodeCarousel = self.head
            while True:
                if( index == indexCome ):
                    if ( field == "title" ):
                        auxNode.carousel.title = value
                        return None
                    elif ( field == "image" ):
                        auxNode.carousel.image = value
                        return None
                    else:
                        return None
                else:
                    auxNode = auxNode.next
                    if auxNode == self.head:
                        break
                    index += 1
            return None
        
    def delete( self, indexCome: int ) -> None:
        index: int = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            auxNode: NodeCarousel = self.head
            while True:
                if( index == indexCome ):
                    if( auxNode == self.head ):
                                            
                        newFirst: NodeCarousel = auxNode.next
                        lastOne: NodeCarousel = auxNode.prev
                        
                        lastOne.next = self.head = newFirst
                        newFirst.prev = lastOne
                        
                        auxNode.prev = auxNode.next = auxNode.carousel = None
                        self.size -= 1
                        return None
                    
                    if( auxNode is not self.head ):
                        predecessor: NodeCarousel = auxNode.prev
                        sucessor: NodeCarousel = auxNode.next
                        predecessor.next = sucessor
                        sucessor.prev = predecessor
                        self.size -= 1
                        auxNode.prev = auxNode.next = auxNode.carousel = None
                        return None
                else:
                    auxNode = auxNode.next
                    if auxNode == self.head:
                        break
                    index += 1
            return None
        
    def findNode( self, indexCome: int ) -> NodeCarousel:
        index: int = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            auxNode: NodeCarousel = self.head
            while True:
                if( index == indexCome ):
                    return auxNode
                else:
                    auxNode = auxNode.next
                    if auxNode == self.head:
                        break
                    index += 1
            return None
        
    def loop(self):
        cur_node: NodeCarousel = self.head
        while cur_node:
            yield cur_node.carousel
            cur_node = cur_node.next
            
            if cur_node == self.head:
                break
            
    def __iter__(self):
        return iter(self.loop())
    
    def createMoviesFromXML(self):
        tree = ET.parse('listaPeliculas.xml')
        root = tree.getroot()

        for categoria in root.findall('categoria'):
            for pelicula in categoria.findall('peliculas/pelicula'):
                title: str = pelicula.find('titulo').text
                image: str = pelicula.find('imagen').text

                carousel:Carousel = Carousel( title, image )

                self.push(carousel)