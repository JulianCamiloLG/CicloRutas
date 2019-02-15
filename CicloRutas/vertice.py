from arista import arista
import random

class vertice:
    def __init__(self, nombre):
        self.nombre = nombre
        self.adyacentes = []
        self.x = 0
        self.y = 0
        self.descripcion = "aca vivmos los cholos"
        self.riesgo = random.randint(1,5)

    def __str__(self):
        toS = "Nombre: " +str(self.getNombre()) + "\n" + "Descripción: " + (self.getDescripcion()) + "\n" + "Riesgo del lugar:" + str(self.getRiesgo()) + "\n" + "Adyacentes: " + str(
            len(self.adyacentes)) + "\n" + "Adyacentes: "+  str(self.adyacentes) + "\n"
        #for n in range(0,len(self.adyacentes)):
         #   toS += "Sitio: " + self.adyacentes[n].getNombre() +"\n"+ "Distancia: " + str(self.adyacentes[n].getPeso()) + "\n"

        return toS

    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion

    def getRiesgo(self):
        return self.riesgo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setRiesgo(self, riesgo):
        self.riesgo = riesgo

    def __getitem__(self, item):
        return item

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getAdyacentes(self):
        return self.adyacentes