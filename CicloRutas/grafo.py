from arista import arista
from vertice import vertice


class grafo:
    def __init__(self):
        self.vertices = []

    def cantidadNodos(self):
        return len(self.vertices)

    def agregarSitio(self, nombre):
        if (self.buscarSitio(nombre) == -1):
            self.vertices.append(vertice(nombre))
            print("agregado exitosamente")
        else:
            print("no agregó")

    def agregarCamino(self, origen, destino, dirigido):
        Origen = self.buscarSitio(origen)
        Destino = self.buscarSitio(destino)
        if Origen != -1 and Destino != -1:
            index=self.vertices.index(Origen)
            self.vertices[index].adyacentes.append(Destino)
            if not (dirigido):
                print('hola :3')
                index=self.vertices.index(Destino)
                self.vertices[index].adyacentes.append(Origen)
            print("camino agregado exitosamente")
        else:
            print("No se pudo agregar")

    def borrarSitio(self, nombre):
        indice = self.buscarSitio(nombre)
        if indice  !=-1:
            self.borrarCaminos(indice.getNombre())
            self.vertices.remove(indice)
            print("borrado")
        else:
            print("no borre")

    def retornarNodo(self, indice):
        return self.vertices[indice]

    def buscarSitio(self, nombre):
        for index, sitio in enumerate(self.vertices):
            sitio = self.vertices[index]
            if sitio.nombre == nombre:
                return sitio
        return -1

    def __str__(self):
        cadena=""
        for i,vertice in  enumerate (self.vertices):
            print(self.vertices[i])
            cadena += grafo[i]

        return cadena

    def __getitem__(self, item):
        return item

    def has_llave(self,index):
        for i in range(0,len(self.vertices)):
            if(i==index):
                return True
        return False


    def borrarCaminos(self, nombre):
          for i in range(0,len(self.vertices)):
                print(i)
                for j in range(0,len(self.vertices[i].adyacentes)):
                    print('el nombre')
                    print(nombre)
                    #print(self.vertices[i].adyacentes[j].getNombre())
                    print(j)
                    if self.vertices[i].adyacentes[j].getNombre()==nombre:
                        indicRemover=self.vertices[i].adyacentes.index(self.vertices[i].adyacentes[j])
                        print(indicRemover)
                        self.vertices[i].adyacentes.remove(self.vertices[i].adyacentes[indicRemover])
                        break;
                    #print (self.vertices[i].adyacentes)


    '''   def todas_las_rutas(self, nodoInicio, nodoFinal):
        caminitop=[]
        todoscaminitops=[]
        caminitop.append(nodoInicio)
        print('uno:' +str(caminitop[0].getNombre()))
        for i in range(1,len(self.vertices)):
            print(nodoInicio.getNombre())
            print(nodoFinal.getNombre())
            for j in range(0, len(self.vertices[i].adyacentes)):
                print(nodoInicio.getNombre())
                print(nodoFinal.getNombre())
                if self.vertices[i].adyacentes[j].getNombre() != nodoFinal.getNombre():
                    indice=self.vertices[i].adyacentes[j]
                    caminitop.append(self.vertices[indice])
                    print('tres: '+str(caminitop))
                    nuevocamino=self.todas_las_rutas(indice, nodoFinal)
                    if nuevocamino:
                        todoscaminitops.append(nuevocamino)

                caminitop.append(nodoFinal)
        todoscaminitops.append(caminitop)
        print('cuatro: '+str(caminitop[0].getNombre()))
        print('cinco: '+str(caminitop[1].getNombre()))
        #print(str(todoscaminitops))
        return todoscaminitops
'''

#Profundidad

#iterativo

    def Profundidad(self, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.vertices[vertex] - visited)
        return visited


    # recursivo
    def ProfundidadRecursivo(graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            dfs(graph, next, visited)
        return visited


    # Anchura
    # iterativo

    def Anchura(graph, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)
        return visited


    # todos los caminos
    def caminosAnchura(self, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next in self.vertices[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    queue.append((next, path + [next]))


    # Djkstra
    def dijsktra(self, initial):
        visited = {initial: 0}
        path = {}

        nodes = set(self.vertices)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.vertices[min_node]:
                weight = current_weight + self.vertices[(min_node, edge)].getRiesgo()
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path
