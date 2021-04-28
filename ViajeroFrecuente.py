class Viajero:
    __numero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas = 0

    def __init__(self, numero = __numero, dni = __dni, nombre = __nombre, apellido = __apellido, millas = __millas):
        self.__numero = numero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas = millas

    def __str__(self):
        return "%d   %s   %s   %s   %d" % (self.__numero, self.__dni, self.__nombre, self.__apellido, self.__millas)

    def obtenerNumero(self):
        return self.__numero

    def obtenerDNI(self):
        return self.__dni

    def obtenerNombre(self):
        return self.__nombre

    def obtenerApellido(self):
        return self.__apellido

    def obtenerMillas(self):
        return self.__millas

    def modificarMillas(self, c):
        self.__millas += c
