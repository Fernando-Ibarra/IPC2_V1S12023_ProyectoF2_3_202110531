import xml.etree.ElementTree as ET
from xml.dom import minidom

from . import Category, NodeCategory
import datastructures.movie as m

class CircularlyLinkedListCategory():

    def __init__(self) -> None:
        """ Create an empty list """
        self.head: NodeCategory = None
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

    def push(self, category: Category) -> bool:
        """push - Add a Category to the back of the list

        Args:
            category (Category): category object
        """
        tempNode: NodeCategory = NodeCategory( category )

        if self.head is None:
            tempNode.next = tempNode
            tempNode.prev = tempNode
            self.head = tempNode
            self.size += 1
            ok = True
            return ok
        else:
            ultimo: NodeCategory = self.head.prev

            tempNode.next = self.head
            tempNode.prev = ultimo

            self.head.prev = tempNode
            ultimo.next = tempNode
            self.size += 1
            ok = True
            return ok
            
    def modify( self, indexCome: int, name: str ) -> None:
        index: int = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            auxNode: NodeCategory = self.head
            while True:
                if( index == indexCome ):
                    auxNode.category.name = name
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
            auxNode: NodeCategory = self.head
            while True:
                if( index == indexCome ):
                    if( auxNode == self.head ):
                                            
                        newFirst: NodeCategory = auxNode.next
                        lastOne: NodeCategory = auxNode.prev
                        
                        lastOne.next = self.head = newFirst
                        newFirst.prev = lastOne
                        
                        auxNode.prev = auxNode.next = auxNode.category = None
                        self.size -= 1
                        return None
                    
                    if( auxNode is not self.head ):
                        predecessor: NodeCategory = auxNode.prev
                        sucessor: NodeCategory = auxNode.next
                        predecessor.next = sucessor
                        sucessor.prev = predecessor
                        self.size -= 1
                        auxNode.prev = auxNode.next = auxNode.category = None
                        return None
                else:
                    auxNode = auxNode.next
                    if auxNode == self.head:
                        break
                    index += 1
            return None
        
    def findNode( self, categoryOne: str ) -> NodeCategory:
        auxNode: NodeCategory = self.head
        while True:
            if( auxNode.category.name == categoryOne ):
                return auxNode
            else:
                auxNode = auxNode.next
                if auxNode == self.head:
                    break
        return None
    
    def findNodeXML( self, indexCome: int ) -> NodeCategory:
        index: int = 1
        if self.head is None:
            print("La lista esta vacía")
        else:
            auxNode: NodeCategory = self.head
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
        cur_node: NodeCategory = self.head
        while cur_node:
            yield cur_node.category
            cur_node = cur_node.next
            
            if cur_node == self.head:
                break
            
    def __iter__(self):
        return iter(self.loop())
        
    def createCategoriesFromXML(self):
        tree = ET.parse('listaPeliculas.xml')
        root = tree.getroot()

        for categoria in root.findall('categoria'):
            name: str = categoria.find('nombre').text
            movies = m.LinkedListMovie()
            for pelicula in categoria.findall('peliculas/pelicula'):
                title: str = pelicula.find('titulo').text
                director: str = pelicula.find('director').text
                year: str = pelicula.find('anio').text
                date: str = pelicula.find('fecha').text
                time: str = pelicula.find('hora').text
                image: str = pelicula.find('imagen').text
                price: int = int(pelicula.find('precio').text)

                movie: m.Movie = m.Movie( title, director, year, date, time, image, price )
                movieNode: m.NodeMovie = m.NodeMovie( movie )

                movies.push(movieNode)

            category: Category = Category(name, movies)
            self.push(category)
            
    def createXMLFromCategories(self):
        open('listaPeliculas.xml', 'w').close()
        categorias = ET.Element('categorias')
        index = 1
        while index <= self.size:
            categoria = ET.SubElement( categorias, 'categoria' )
            node = self.findNodeXML( index )
            nombreD = node.category.name
            nombreC = ET.SubElement( categoria, 'nombre' )
            nombreC.text = nombreD
            internalIndex = 1
            peliculas = ET.SubElement( categoria, 'peliculas' )
            while internalIndex <= node.category.movies.size + 1:
                movie: m.Movie = node.category.movies.findMovie(internalIndex)
                pelicula = ET.SubElement( peliculas, 'pelicula' )
                nombre = ET.SubElement( pelicula, 'nombre' )
                nombre.text = movie.title
                director = ET.SubElement( pelicula, 'director' )
                director.text = movie.director
                anio = ET.SubElement( pelicula, 'anio' )
                anio.text = movie.year
                fecha = ET.SubElement( pelicula, 'fecha' )
                fecha.text = movie.date
                hora = ET.SubElement( pelicula, 'hora' )
                hora.text = movie.date
                imagen = ET.SubElement( pelicula, 'imagen' )
                imagen.text = movie.image
                precio = ET.SubElement( pelicula, 'precio' )
                precio.text = str(movie.price)
                internalIndex += 1
            index += 1
        rough_string = ET.tostring(categorias, 'utf-8')
        reparsed = minidom.parseString( rough_string )
        file = open('listaPeliculas.xml', 'w')
        file.write(reparsed.toprettyxml(indent=" "))
        file.close()