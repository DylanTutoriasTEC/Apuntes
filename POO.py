class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad):
        self.validarentrada(nombre, edad)
        
        self.set_nombre(nombre)
        self.set_edad(edad)

    # Métodos de la clase
    def validarentrada(self, nombre, edad):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser una cadena.")
        if not (isinstance(edad, int) and edad > 0):
            raise ValueError("La edad debe ser un número entero positivo.")
        
    def saludar(self):
        print(f"Hola, mi nombre es {self.get_nombre()} y tengo {self.get_edad()} años.")

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad
