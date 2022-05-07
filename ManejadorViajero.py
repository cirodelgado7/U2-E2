import csv
from ViajeroFrecuente import ViajeroFrecuente


class Manejador:

    __listaViajeros = []

    def __init__(self):
        self.__listaViajeros = []

    def __str__(self):
        s = ""
        for lista in self.__listaViajeros:
            s += str(lista) + '\n'
        return s

    def testViajeros(self):
        archivo = open('ViajeroFrecuente.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                numero = int(fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas = int(fila[4])
                unViajero = ViajeroFrecuente(numero, dni, nombre, apellido, millas)
                self.agregarViajeros(unViajero)
        archivo.close()
        print('\n ***** Lista de Viajeros Frecuentes *****')
        print(self.__str__())

    def agregarViajeros(self, unViajero):
        self.__listaViajeros.append(unViajero)

    def buscarViajero(self, clave):
        for indice, ViajeroFrecuente in enumerate(self.__listaViajeros):
            if ViajeroFrecuente.obtenerNumero() == clave:
                return indice

    def obtenerViajero(self, indice):
        return self.__listaViajeros[indice]

    def cantidadTotaldeMillas(unViajero):
        return ViajeroFrecuente.obtenerMillas(unViajero)

    def acumularMillas(unViajero, cantidad):
        ViajeroFrecuente.modificarMillas(unViajero, cantidad)
        return ViajeroFrecuente.obtenerMillas(unViajero)

    def canjearMillas(unViajero, cantidad):
        if ViajeroFrecuente.obtenerMillas(unViajero) >= cantidad:
            ViajeroFrecuente.modificarMillas(unViajero, - cantidad)
            print('\n El canje se realizó con éxito ')
        else:
            print('\n La cantidad de millas que dispone es insuficiente para realizar el canje \n')
        return ViajeroFrecuente.obtenerMillas(unViajero)