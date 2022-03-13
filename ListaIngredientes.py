from nodoIngredientes import NodoIngredientes
from prettytable import PrettyTable

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
        x = PrettyTable()
        x.field_names = ["Nombre ingrediente","Tiempo"]
        print("============== TABLA DE INGREDIENTES==============")
        x.add_row([f'{head.ingrediente.nombre}', f'{head.ingrediente.tiempo} minutos'])
        
        while head.siguiente != None:
            head = head.siguiente
            x.add_row([f'{head.ingrediente.nombre}', f'{head.ingrediente.tiempo} minutos'])
        print(x)
        
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





        
        