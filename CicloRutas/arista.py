import random
class arista:
    def __init__(self, nombre):
        self.peso = random.randint(0,200)
        self.nombre = nombre
        self.x = 0
        self.y = 0
        self.popularidad = 0
        self.accidentalidad = 0

    def getNombre(self):
        return self.nombre

    def getPeso(self):
        return self.peso

    def __str__(self):
        cadena = "Nombre: " + self.getNombre() + "\n" + "Peso: " +str(self.getPeso()) + "\n"