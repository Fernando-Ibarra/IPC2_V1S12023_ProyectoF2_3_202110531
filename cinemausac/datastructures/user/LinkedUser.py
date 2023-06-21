import xml.etree.ElementTree as ET
from xml.dom import minidom

from .NodeUser import NodeUser, User

class LinkedUser(object):
    
    def __init__(self) -> None:
        """ Create an empty stack """
        self.head: NodeUser = None
        self.tail: NodeUser = None
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
    
    
    # Add User
    def push(self, node: NodeUser) -> None:
        """Add a new Node to the back of the stack

        Args:
            e (NodeUser): User node
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
        cur_node: NodeUser = self.head
        while cur_node:
            yield cur_node.user
            cur_node = cur_node.next
            
    def __iter__(self):
        return iter(self.loop())
    
    def findToValidate( self, email:str, password: str):
        auxNode = self.head
        while auxNode is not None:
            if auxNode.user.password == password and auxNode.user.email == email:
               ok=True
               return auxNode.user, ok
            auxNode = auxNode.next
        ok = False
        return None, ok
    
    def findUser( self, indexCome: int ) -> User:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode.user
            else:
                auxNode = auxNode.next
                index += 1
        return None
    
    def findNode( self, indexCome: int ) -> NodeUser:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if ( index == indexCome ):
                return auxNode
            else:
                auxNode = auxNode.next
                index += 1
        return None
    
    def deleteUser( self, indexCome: int ) -> None:
        deleteNode: NodeUser = self.findNode( indexCome )
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

    def modifyUser( self, indexCome: int, field: str, value ) -> None:
        index: int = 1
        auxNode = self.head
        while auxNode is not None:
            if( index == indexCome ):
                if ( field == "name" ):
                    auxNode.user.name = value
                    return None
                elif ( field == "lastName" ):
                    auxNode.user.lastName = value
                    return None
                elif ( field == "phoneNUmber" ):
                    auxNode.user.phoneNUmber = value
                    return None
                elif ( field == "email" ):
                    auxNode.user.email = value
                    return None
                elif ( field == "password" ):
                    auxNode.user.password = value
                    return None
                elif ( field == "rol" ):
                    auxNode.user.rol = value
                    return None
                else:
                    return None
            else:
                auxNode = auxNode.next
                index += 1

    def createUserFromXML(self) -> None:
        tree = ET.parse('listaUsuarios.xml')
        root = tree.getroot()

        for usuario in root.findall('usuario'):
            name: str = usuario.find('nombre').text
            lastName: str = usuario.find('apellido').text
            phoneNumber: str = usuario.find('telefono').text
            email: str = usuario.find('correo').text
            password: str = usuario.find('contrasena').text
            rol: str = usuario.find('rol').text

            user: User = User( name, lastName, phoneNumber, email, password, rol)
            nodeUser: NodeUser = NodeUser( user )
            self.push( nodeUser )
            
    def createXMLFromUser( self ) -> None:
        open('listaUsuarios.xml', 'w').close()
        usuarios = ET.Element('usuarios')
        index = 1
        while index <= (self.size + 1) :
            node = self.findNode( index )
            nombreU = node.user.name
            apellidoU = node.user.lastName
            telefonoU = node.user.phoneNUmber
            correoU = node.user.email
            contrasenaU = node.user.password
            rolU = node.user.rol

            usuario = ET.SubElement( usuarios, 'usuario' )
            rol = ET.SubElement( usuario, 'rol' )
            rol.text = rolU
            nombre = ET.SubElement( usuario, 'nombre' )
            nombre.text = nombreU
            apellido = ET.SubElement( usuario, 'apellido' )
            apellido.text = apellidoU
            telefono = ET.SubElement( usuario, 'telefono' )
            telefono.text = telefonoU
            correo = ET.SubElement( usuario, 'correo' )
            correo.text = correoU
            contrasena = ET.SubElement( usuario, 'contrasena' )
            contrasena.text = contrasenaU
            index +=1
        rough_string = ET.tostring(usuarios, 'utf-8')
        reparsed = minidom.parseString( rough_string )
        file = open('listaUsuarios.xml', 'w')
        file.write(reparsed.toprettyxml(indent=" "))
        file.close()
