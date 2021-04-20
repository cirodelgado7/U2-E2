import sys
from ManejadorViajero import Manejador

class Menu:
    indice = 0
    def __init__(self):
        self.__mv = Manejador()
        self.__mv.testViajeros()
        self.__elecciones = {
            "1": self.consultarMillas,
            "2": self.acumularMillas,
            "3": self.canjearMillas,
            "4": self.salir
            }
    
    def mostrarMenu(self):
        print("\n Selecciona una opción")
        print(" 1 - Consulta cantidad de millas")
        print(" 2 - Acumular millas")
        print(" 3 - Canjear millas")
        print(" 4 - Salir")

    def run(self):
        while True:
            print('Listado de Viajeros')
            print(self.__mv)
            n = int(input(' Numero de Viajero: '))
            i = self.__mv.buscarViajero(n)
            getIndice.indice = i
            print('{}'.format(getIndice.indice))
            self.mostrarMenu()
            eleccion = input(" Opción: ")
            accion = self.__elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print('La opcion {0} elegida no es valida, solo de aceptan numeros del 1 al 4'.format(eleccion))

    def consultarMillas(self):
        print('{}'.format(self.__mv.obtenerViajero(i)))

        print('\t *****Esta opción está en Construcción*****')
    
    
    def acumularMillas(self, i):
        print('\t *****Esta opción está en Construcción*****')
    
    
    def canjearMillas(self, i):
        print('\t *****Esta opción está en Construcción*****')
    
    
    def salir(self):
        sys.exit(0)

    @classmethod
    def getIndice(cls):
        return cls.indice