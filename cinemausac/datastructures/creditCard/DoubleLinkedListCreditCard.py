import xml.etree.ElementTree as ET
from xml.dom import minidom

from .NodeCreditCard import CreditCard, NodeCreditCard

class DoubleLinkedListCreditCard(object):
    
    def __init__( self ) -> None:
        """ Create an empty list """
        self.head: NodeCreditCard = NodeCreditCard( None, None, None )
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
       
    def push( self, creditCard: CreditCard ) -> bool:
        """push - Add a MovieRoom to the back of the list

        Args:
            CreditCard (CreditCard): CreditCard object
        """
        newest: NodeCreditCard = NodeCreditCard( creditCard )
        if self.head is None:
            self.head = newest
        else:
            current: NodeCreditCard = self.head
            
            while current.next is not None:
                current = current.next
            current.next = newest
            newest.prev = current
            self.size += 1
            ok = True
            return ok
    
    def deleteNode( self, node: NodeCreditCard ) -> None:
        """deleteNode Delete node from the list

        Args:
            node (NodeCreditCard): movieRoom object
        """
        predecessor: NodeCreditCard = node.prev
        sucessor: NodeCreditCard = node.next
        if( node.next is None ):
            sucessor = None
            predecessor.next = sucessor
            self.size -= 1
        else:
            predecessor.next = sucessor
            sucessor.prev = predecessor
            self.size -= 1
        # deprecate Node
        node.prev = node.next = node.creditcard = None
        return None
        
    def modifyCard( self, indexCome: int, field: str, value  ):
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                if ( field == "type" ):
                    auxNode.creditcard.type = value
                    return None
                elif ( field == "number" ):
                    auxNode.creditcard.number = value
                    return None
                if ( field == "owner" ):
                    auxNode.creditcard.owner = value
                    return None
                elif ( field == "expiredTime" ):
                    auxNode.creditcard.expiredTime = value
                    return None
                else:
                    return None
            else:
                auxNode = auxNode.next
                index += 1
            
    def findNode( self, indexCome: int ) -> NodeCreditCard:
        index: int = 1
        auxNode: NodeCreditCard = self.head
        while auxNode is not None:
            if( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next
                index += 1
        return None
    
    def loop(self):
        cur_node: NodeCreditCard = self.head
        while cur_node:
            yield cur_node.creditcard
            cur_node = cur_node.next
            
    def __iter__(self):
        return iter(self.loop())

    def createCardFromXML( self ) -> None:
        tree = ET.parse('listaTarjetas.xml')
        root = tree.getroot()

        for tarjeta in root.findall('tarjeta'):
            typeC: str = tarjeta.find('tipo').text
            number: str = tarjeta.find('numero').text
            owner: str = tarjeta.find('titular').text
            expiredTime: str = tarjeta.find('fecha_expiracion').text
            creditCard: CreditCard = CreditCard( typeC, number, owner, expiredTime )
            self.push( creditCard )

    def createXMLFromCard(self) -> None:
        open('listaTarjetas.xml', 'w').close()
        tarjetas = ET.Element('tarjetas')
        index = 1
        while index <= (self.size + 1):
            node = self.findNode( index )
            tarjeta = ET.SubElement( tarjetas, 'tarjeta' )
            tipo = ET.SubElement( tarjeta, 'tipo' )
            tipo.text = node.creditcard.type
            numero = ET.SubElement( tarjeta, 'numero' )
            numero.text = node.creditcard.number
            titular = ET.SubElement( tarjeta, 'titular' )
            titular.text = node.creditcard.owner
            fecha_expiracion = ET.SubElement( tarjeta, 'fecha_expiracion' )
            fecha_expiracion.text = node.creditcard.expiredTime
            index += 1
        rough_string = ET.tostring(tarjetas, 'utf-8')
        reparsed = minidom.parseString( rough_string )
        file = open('listaTarjetas.xml', 'w')
        file.write(reparsed.toprettyxml(indent=" "))
        file.close()