import sys, os
from ManejadorViajero import Manejador

class Menu:

    __switcher = None

    def __init__(self):
        __switcher = None
        self.__switcher = {
            1: self.consultarM,
            2: self.acumularM,
            3: self.canjearM,
            4: self.salir
            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self,op,unViajero):
        func = self.__switcher.get(op,lambda: print("Opción no válida"))
        func(unViajero)

    def consultarM(self,unViajero):
        m = Manejador.cantidadTotaldeMillas(unViajero)
        print('\n El viajero tiene {} millas disponibles \n'.format(m))
        os.system('pause')

    def acumularM(self,unViajero):
        c = int(input('\n Cantidad de millas recorridas: '))
        a = Manejador.acumularMillas(unViajero,c)
        print('\n El viajero acumuló {} millas \n'.format(a))
        os.system('pause')

    def canjearM(self,unViajero):
        c = int(input('\n Ingrese la cantidad de millas a canjear: '))
        m = Manejador.canjearMillas(unViajero,c)
        print('\n El Viajero dispone de {} millas para canjear \n'.format(m))
        os.system('pause')

    def salir(self,unViajero):
        sys.exit(0)