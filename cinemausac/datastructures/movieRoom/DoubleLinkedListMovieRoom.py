from .NodeMovieRoom import NodeMovieRoom, MovieRoom

class DoubleLinkedListMovieRoom(object):
    
    def __init__( self ) -> None:
        """ Create an empty list """
        self.head: NodeMovieRoom = NodeMovieRoom( None, None, None )
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
        return self.size == 0
       
    def push( self, movieRoom: MovieRoom ) -> bool:
        """push - Add a MovieRoom to the back of the list

        Args:
            movieRoom (MovieRoom): movieRoom object
        """
        newest: NodeMovieRoom = NodeMovieRoom( movieRoom )
        if self.head is None:
            self.head = newest
        else:
            current: NodeMovieRoom = self.head
            
            while current.next is not None:
                current = current.next
            current.next = newest
            newest.prev = current
            self.size += 1
            ok = True
            return ok
    
    def deleteNode( self, node: NodeMovieRoom ) -> None:
        """deleteNode Delete node from the list

        Args:
            node (NodeMovieRoom): movieRoom object
        """
        predecessor: NodeMovieRoom = node.prev
        sucessor: NodeMovieRoom = node.next
        if( node.next is None ):
            sucessor = None
            predecessor.next = sucessor
            self.size -= 1
        else:
            predecessor.next = sucessor
            sucessor.prev = predecessor
            self.size -= 1
        # deprecate Node
        node.prev = node.next = node.movieRoom = None
        return None
        
    def modifyMovieRoom( self, indexCome: int, field: str, value  ):
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                if ( field == "number" ):
                    auxNode.movieRoom.number = value
                    return None
                elif ( field == "seats" ):
                    auxNode.movieRoom.seats = value
                    return None
                else:
                    return None
            else:
                auxNode = auxNode.next
                index += 1
                
    def returnMovieRoom( self, indexCome: int ):
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                return auxNode.movieRoom.number, auxNode.movieRoom.seats 
            else:
                auxNode = auxNode.next
                index += 1
    
    def findNode( self, indexCome: int ) -> NodeMovieRoom:
        index: int = 1
        auxNode: NodeMovieRoom = self.head
        while auxNode is not None:
            if( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next
                index += 1
        return None
    
    def findRoomByName( self, room: str ) -> MovieRoom:
        auxNode: NodeMovieRoom = self.head
        while auxNode is not None:
            if( auxNode.movieRoom.number == room ):
                return auxNode.movieRoom
            else:
                auxNode = auxNode.next
        return None
    
    def loop(self):
        cur_node: NodeMovieRoom = self.head
        while cur_node:
            yield cur_node.movieRoom
            cur_node = cur_node.next
            
    def __iter__(self):
        return iter(self.loop())