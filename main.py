from nodoIngredientes import NodoIngredientes
from ingredientes import Ingredientes
from ListaIngredientes import listaIngredientes
from ColaOrdenes import  ColaOrdenes
from ordenNueva import Orden

ListaI = listaIngredientes()
OrdenN = ColaOrdenes()

#Agregando ingredientes y sus tiempos
ListaI.AgregarIngrediente(Ingredientes('Pepperoni',3))
ListaI.AgregarIngrediente(Ingredientes('Salchicha',4))
ListaI.AgregarIngrediente(Ingredientes('Carne',10))
ListaI.AgregarIngrediente(Ingredientes('Queso',5))
ListaI.AgregarIngrediente(Ingredientes('Piña',2))

#Verificando que se agregaron los ingredientes
#ListaI.ImprimirIngredientes()

while True:

    print("================= Menú de órdenes =================")
    print("1. Agregar órden a la cola")
    print("2. Entregar órden a la cola")
    print("3. Mostar datos")
    print("4. Salir")

    opcion = int(input())

    if opcion == 1:
        print("Ingrese el nombre del cliente:")
    
        nombre = input()
        print("")
        print("Ingres la cantidad de Pizzas:")
        cantidad = int(input())

        while True:
            ListaI.ImprimirIngredientes()

            print('Ingrese el nombre de un ingrediente para sus pizzas:')
            nombrei = input()
            print("")
            ing = ListaI.ObtenerIngrediente(nombrei)

            if ing == None:
                print("Ingrediente no existe, ingrese un ingrediente correcto.\n")
            else:
                break
        OrdenN.AgregarOrden(Orden(nombre,cantidad, ing))

        print('¡Orden agregada!')
        OrdenN.imprimirOrden()
        OrdenN.AgregarIm()
    elif opcion == 2:
        print('Orden despachada...')
        OrdenN.QuitarOrden()

    elif opcion == 3:
        print("Nombre: Gabriel Enrique Perez Meza \n Carne: 201900221")
        
    elif opcion == 4:

        print('Saliendo............')
        break
    else:
        print('Ingrese una opcioón válida')
        

    

