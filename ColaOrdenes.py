from nodoOrdenes import NodoOrdenes

class ColaOrdenes:
    def __init__(self):
        self.head = None
        self.last = None
    
    def AgregarOrden(self,orden):
        if not self.head:
            self.head = NodoOrdenes(orden)
            self.last = NodoOrdenes(orden)
        else:
            self.last.siguiente = NodoOrdenes(orden)
            self.last = NodoOrdenes(orden)
    
    def QuitarOrden(self):
        cantidad = self.head.orden.cantidad
        tiempo = self.head.orden.ingrediente.tiempo
        total = cantidad * tiempo
        self.Tiempo(total)
        self.head = self.head.siguiente
    
    def Tiempo(self,tiempo):
        head = self.head
        while head.siguiente != None:
            head = head.siguiente
            head.orden.tiempoEspera += tiempo


