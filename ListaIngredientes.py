from nodoIngredientes import NodoIngredientes

class listaIngredientes:
    def __init__(self):
        self.head = None

    def AgregarIngrediente(self, ingrediente):
        if not self.head:
            self.head = NodoIngredientes(ingrediente)
        else:
            head = self.head
            while head.siguiente != None:
                head = head.siguiente
            head.siguiente = NodoIngredientes(ingrediente)

    def ImprimirIngredientes(self):
        head = self.head
        print(f'Nombre: {head.ingrediente.nombre}')
        print(f'Tiempo: {head.ingrediente.tiempo}')
        while head.siguiente != None:
            head = head.siguiente
            print(f'Nombre: {head.ingrediente.nombre}')
            print(f'Tiempo: {head.ingrediente.tiempo} minutos')
    
    def ObtenerIngrediente(self,nombre):
        head = self.head
        if nombre == head.ingrediente.nombre:
            return head.ingrediente
        else:
            while head.siguiente != None:
                head = head.siguiente
                if nombre == head.ingrediente.nombre:
                    return head.ingrediente
            return None





        
        