from ManejadorViajero import Manejador
from MenuViajero import Menu

if __name__ == '__main__':
    mv = Manejador()
    mv.testViajeros()
    print('\n ***** Lista de Viajeros Frecuentes *****')
    print(mv)
    n = int(input('Numero de Viajero: '))
    while True:
        try:
            if n in range(1000,1010):
                i = mv.buscarViajero(n)
                k = mv.obtenerViajero(i)
                menu = Menu()
                break
            else:
                print('***** El numero de viajero ingresado no es valido *****')
                print('***** Ingrese números de viajero de 1000 a 1009 *****')
                n = int(input('Numero de Viajero: '))
        except (ValueError): print('***** Ingrese números de viajero de 1000 a 1009 *****')
    salir = False
    while not salir:
        print("\n-----------------Menu--------------------")
        print(" 1 - Consulta cantidad de millas")
        print(" 2 - Acumular millas")
        print(" 3 - Canjear millas")
        print(" 4 - Salir")
        op = int(input('Ingrese una opcion: '))
        if op in range(1,5):
            menu.opcion(op,k)
        else:
            print('Opción no valida - Elija nuevamente la opción')
