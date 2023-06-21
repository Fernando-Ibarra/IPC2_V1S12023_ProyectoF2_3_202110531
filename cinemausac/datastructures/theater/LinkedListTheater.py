import xml.etree.ElementTree as ET
from xml.dom import minidom

import datastructures.movieRoom as mr
from . import NodeTheater, Theater

class LinkedListTheater(object):
    
    def __init__( self ) -> None:
        self.head: NodeTheater = None
        self.tail: NodeTheater = None
        self.size: int = 0
        
    def __len__(self) -> int:
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
        return self.tail == None
    
    # Add Category
    def push(self, node: NodeTheater) -> None:
        """Add a new Node to the back of the stack

        Args:
            e (NodeCategory): Category node
        """
        newNode = node
        if self.isEmpty():
            self.tail = self.head = newNode
        else:
            auxNode = self.head
            while auxNode.next is not None:
                auxNode = auxNode.next
            auxNode.next = newNode
            self.size += 1
            ok = True
            return ok
        
    def loop(self):
        cur_node: NodeTheater = self.head
        while cur_node:
            yield cur_node.theater
            cur_node = cur_node.next
    
    def __iter__(self):
        return iter(self.loop())
            
    def findTheater( self, indexCome: int ) -> Theater:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode.theater
            else:
                auxNode = auxNode.next
                index += 1
        return None
    
    def findNode( self, indexCome: int ) -> NodeTheater:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next
                index += 1
        return None
    
    def findNodeByName( self, name: str ) -> NodeTheater:
        auxNode = self.head
        while auxNode is not None:
            if ( auxNode.theater.nombre == name ):
                return auxNode
            else:
                auxNode = auxNode.next
        return None
    
    def deleteTheater( self, indexCome: int ) -> None:
        deleteNode: NodeTheater = self.findNode( indexCome )
        if ( deleteNode is not None):
            auxNode = self.head
            while auxNode is not None:
                if( auxNode.next == deleteNode ): 
                    if( deleteNode is not None ):
                        tempNode = deleteNode.next 
                        auxNode.next = tempNode
                        deleteNode = None
                        self.size -= 1
                    else:
                        return None
                auxNode = auxNode.next
            return None
        else:
            return None
        
    def modifyTheater( self, indexCome: int, name: str) -> None:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                auxNode.theater.name = name
                return None
            else:
                auxNode = auxNode.next
                index += 1
        return None

    def createTheatersFromXML( self ) -> None:
        tree = ET.parse('listaCines.xml')
        root = tree.getroot()

        for cine in root.findall('cine'):
            name: str = cine.find('nombre').text
            room = mr.DoubleLinkedListMovieRoom()
            for sala in cine.findall('salas/sala'):
                number: str = sala.find('numero').text
                seats: int = int(sala.find('asientos').text)
                movieRoom: mr.MovieRoom = mr.MovieRoom(number, seats)
                room.push(movieRoom)
            theater: Theater = Theater(name, room)
            nodeTheater: NodeTheater = NodeTheater(theater)
            self.push( nodeTheater )

    def createXMLFromTheaters(self) -> None:
        open('ListaCines.xml', 'w').close()
        cines = ET.Element('cines')
        index = 1
        while index <= (self.size + 1):
            node = self.findNode( index )
            cine = ET.SubElement( cines, 'cine' )
            nombre = ET.SubElement( cine, 'nombre' )
            nombre.text = node.theater.name
            salas = ET.SubElement( cine, 'salas' )
            internalIndex = 1
            lim = node.theater.rooms.size
            print(f"LIMITE { lim }")
            room = node.theater.rooms
            while internalIndex <= lim:
                node = room.findNode( internalIndex )
                if( node.movieRoom is None ):
                    internalIndex += 1
                else:
                    number = node.movieRoom.number
                    seats = node.movieRoom.seats
                    sala = ET.SubElement( salas, 'sala' )
                    numero = ET.SubElement( sala, 'numero' )
                    numero.text = number
                    asientos = ET.SubElement( sala, 'asientos' )
                    asientos.text = str(seats)
                    internalIndex += 1
            index += 1
        rough_string = ET.tostring(cines, 'utf-8')
        reparsed = minidom.parseString( rough_string )
        file = open('ListaCines.xml', 'w')
        file.write(reparsed.toprettyxml(indent=" "))
        file.close()