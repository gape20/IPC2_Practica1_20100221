from matplotlib.image import imread
from nodoOrdenes import NodoOrdenes
from os import system
import os


class ColaOrdenes:
    def __init__(self):
        self.head = None
       
    def AgregarOrden(self,orden):
        if not self.head:
            self.head = NodoOrdenes(orden)
        else:
            head = self.head
            while head.siguiente != None:
                head = head.siguiente
            head.siguiente = NodoOrdenes(orden)
           
        return orden
    
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

    def imprimirOrden(self):
        head = self.head
        print(f'Orden nueva a nombre de: {head.orden.nombre}')
        print(f'Tiempo de preparacion: {head.orden.ingrediente.tiempo * head.orden.cantidad} minutos')
        print(f'Tiempo de espera: {head.orden.tiempoEspera} minutos')
        while head.siguiente != None:
            head = head.siguiente
            print(f'Orden nueva a nombre de {head.orden.nombre}')
            print(f'Tiempo de preparacion: {head.orden.ingrediente.tiempo * head.orden.cantidad} minutos')
            print(f'Tiempo de espera: {head.orden.tiempoEspera} minutos')

    def AgregarIm(self):
        head = self.head
        orden = ''
        orden += "Nombre: "
        orden += head.orden.nombre
        orden += "\t Ingrediente de Pizzas: " 
        orden += head.orden.ingrediente.nombre
        orden += "\t Tiempo en la cocina: "
        orden +=f'{str(head.orden.ingrediente.tiempo * head.orden.cantidad)} min.'
        orden += "\t Tiempo de espera: "
        orden += f'{str(head.orden.tiempoEspera)} min.'
        centro = ''
        archivo = open("C:/Users/User/Downloads/cola.dot", 'w')
        aux = 0
        aux2=1
        a = '''digraph G {

  subgraph cluster_0 {
    style=filled;
    color=lightgrey;
    node [style=filled,color=white];
    '''
        centro+= f'{aux}[shape=ellipse,color=red,style=bold, label="{orden}", labelloc=b]\n'
        
        while head.siguiente != None:
            aux2+=1
            head = head.siguiente
            orden = ''
            orden += "Nombre: "
            orden += head.orden.nombre
            orden += "\t Ingrediente de Pizzas: " 
            orden += head.orden.ingrediente.nombre
            orden += "\t Tiempo en la cocina: "
            orden +=f'{str(head.orden.ingrediente.tiempo * head.orden.cantidad)} min.'
            orden += "\t Tiempo de espera: "
            orden += f'{str(head.orden.tiempoEspera)} min.'
            centro+= f'{aux2}[shape=ellipse,color=red,style=bold, label="{orden}", labelloc=b]\n'
            centro+=f'{aux}->{aux2}'
        centro+="\n"
        centro += 'label = "Cola de ordenes"'
        centro +='}'
        centro +='}'
        
        archivo.write(a)
        archivo.write(centro)
        archivo.close()
        os.chdir('C:/Users/User/Downloads')
       
        os.system('dot -Tpng cola.dot -o cola.png')

        os.system('"cola.png"')