from grafo import grafo
from vertice import vertice
from arista import arista
from tkinter import *
from tkinter import ttk
import math
import time

grafito = grafo()
grafito.agregarSitio("la norte")
grafito.agregarSitio("aranjuez")
grafito.agregarSitio("pereira")
grafito.agregarSitio("lab")

grafito.agregarCamino("la norte", "aranjuez", TRUE)
grafito.agregarCamino("aranjuez", "pereira",  TRUE)
grafito.agregarCamino("la norte", "pereira",  TRUE)
grafito.agregarCamino("la norte","lab",TRUE)
grafito.agregarCamino("lab","pereira", TRUE)
grafito.agregarCamino("lab","aranjuez",TRUE)


grafito.vertices[0].setX(100)
grafito.vertices[1].setX(200)
grafito.vertices[2].setX(150)
grafito.vertices[3].setX(200)
grafito.vertices[0].setY(100)
grafito.vertices[1].setY(100)
grafito.vertices[2].setY(300)
grafito.vertices[3].setY(300)

#print(grafito.dijsktra("la norte"))
#print(list(grafito.caminosAnchura(0,1)))
print(grafito.cantidadNodos())
for i in range(0, 4):
    print(grafito.vertices[i])
    print('------------------')

'''grafito.borrarSitio("aranjuez")
for j in range(0, len(grafito.vertices)):
 #  print(grafito.vertices[j])
    print('------------------')'''




def todas_las_rutitas(vertices,indiInicio, indiFin, camino=[]):
        print (vertices)
        camino=camino+[indiInicio]
        if indiInicio==indiFin:
            return camino

        if indiInicio is not  vertices[vertices.index(indiInicio)]:
            print('sisas')
            return []

        caminos=[]
        for vertice in vertices[0]:
            if vertice not in camino:
                hijo_caminos=todas_las_rutitas(vertices,vertice, indiFin, camino)
                for hijo_camino in hijo_caminos:
                    caminos.append(hijo_camino)
        return caminos



#print(grafito.todas_las_rutas(grafito.vertices[0], grafito.vertices[3]))

'''def find_all_paths(graph, start, end, path=[]):
    if path is None:
        path = [start]

    if start == end:
        yield path

    for vertex in [x for x in graph.[start] if x not in path]:
        for each_path in find_all_paths(graph,vertex,end,path+[vertex]):
            yield each_path

print(list(find_all_paths(grafito,0,3)))
'''

def cargar_grafo():
    checkButtonCrear.config(state=DISABLED)
    checkButtonCrearlin.config(state=DISABLED)
    for i in range(0, len(grafito.vertices)):
        panel.create_rectangle(grafito.vertices[i].getX(), grafito.vertices[i].getY(), grafito.vertices[i].getX() + 25,
                               grafito.vertices[i].getY() + 25, fill='white')
        panel.create_text(grafito.vertices[i].getX() + 10, grafito.vertices[i].getY() - 6.25, text=grafito.vertices[i].getNombre())
    crear_lineas()
    panel.update()


def crear_lineas():
    for i in range(0, len(grafito.vertices)):
        aux = grafito.vertices[i]
        if aux.adyacentes is not None:
            for j in range(0, len(aux.adyacentes)):
                panel.create_line(aux.getX() + 12.5, aux.getY() + 12.5, aux.adyacentes[j].getX() + 12.5,
                                  aux.adyacentes[j].getY() + 12.5, fill='red')

cuadros = []
nodito = NONE
grafito2 = grafo()

def dibujarNodos(event):
    x = event.x
    y = event.y
    if grafito2.vertices == []:
            panel.create_rectangle(x + 12.5, y + 12.5, x - 12.5, y - 12.5, fill='white', outline='black')
            nombre = input('ingrese el nombre: ')
            grafito2.agregarSitio(nombre)
            grafito2.vertices[0].setX(x)
            grafito2.vertices[0].setY(y)
            panel.create_text(x, y-18, text=nombre)
            panel.update()
    else:

            # nombre=crearEntrada()
            # if nombre is not NONE:
            nombre = input('Ingreselo pa: ')
            grafito2.agregarSitio(nombre)
            panel.create_rectangle(x + 12.5, y + 12.5, x - 12.5, y - 12.5, fill='white', outline='black')
            for i in range(0, len(grafito2.vertices)):
                   if grafito2.vertices[i].getNombre() == nombre:
                     grafito2.vertices[i].setX(x)
                     grafito2.vertices[i].setY(y)
                     print(grafito2.vertices[i].getX())
                     print(grafito2.vertices[i].getY())
            panel.create_text(x, y-18, text=nombre)
            panel.update()



    print(str(grafito2.vertices[0].getX())+ grafito2.vertices[0].getNombre())

listanodos=[]
listax=[]
listay=[]

def agregarCaminos(event):
        listanodos.append(buscar_por_click(event.x))
        if(len(listanodos)==2):
                nodoOrigen = listanodos[0]
                nodoDestino = listanodos[1]
                print('coord x: '+str(nodoOrigen.getX()))
                print('coord'+str(nodoDestino.getX()))
                print(nodoOrigen)
                print(nodoDestino)
                panel.create_line(nodoOrigen.getX(), nodoOrigen.getY(), nodoDestino.getX(), nodoDestino.getY(), fill='red')
                panel.update()
                grafito2.agregarCamino(nodoOrigen.getNombre(), nodoDestino.getNombre(), True)
                listanodos.clear()
                #print(listanodos)



listaMenores=[]

def habilitar():
    checkButtonCrear.config(state=NORMAL)
    checkButtonCrearlin.config(state=NORMAL)
    checkButtonEliminar.config(state=NORMAL)

def eiminar(event):
    nodoaEliminar=buscar_por_click(event.x)
    print(nodoaEliminar)
    grafito2.borrarSitio(nodoaEliminar.getNombre())
    panel.delete(ALL)
    cargar_grafo2()

def cargar_grafo2():
    for i in range(0, len(grafito2.vertices)):
        panel.create_rectangle(grafito2.vertices[i].getX(), grafito2.vertices[i].getY(), grafito2.vertices[i].getX() + 25,
                               grafito2.vertices[i].getY() + 25, fill='white')
        panel.create_text(grafito2.vertices[i].getX() + 10, grafito2.vertices[i].getY() - 6.25, text=grafito2.vertices[i].getNombre())
    crear_lineas2()
    panel.update()

def crear_lineas2():
     for i in range(0, len(grafito2.vertices)):
        aux = grafito2.vertices[i]
        if aux.adyacentes is not None:
            for j in range(0, len(aux.adyacentes)):
                panel.create_line(aux.getX() + 12.5, aux.getY() + 12.5, aux.adyacentes[j].getX() + 12.5,
                                  aux.adyacentes[j].getY() + 12.5, fill='red')

def buscar_por_click(x):
    menor=99999
    for i in range(0, len(grafito2.vertices)):
        x1=grafito2.vertices[i].getX()
        print(x)
        print(x1)
        resta=(abs(x1-x))
        listaMenores.append(resta)
        print(resta)
        print(listaMenores)
    for j in range(0,len(listaMenores)):
           if listaMenores[j]< menor:
               menor=listaMenores[j]
               indicemenor=listaMenores.index(listaMenores[j])

    aux = grafito2.vertices[indicemenor]
    listaMenores.clear()
    print(aux)
    return aux

def funcion_de_funciones(event):
    if casoPintar.get() == 1:
        checkButtonEliminar.deselect()
        checkButtonEliminar.deselect()
        dibujarNodos(event)

    elif casoLineas.get() ==1:
        checkButtonEliminar.selection_clear()
        checkButtonCrear.deselect()
        agregarCaminos(event)

    elif CasoEliminar.get()==1:
        checkButtonCrear.deselect()
        checkButtonCrearlin.deselect()
        eiminar(event)



def crearEntrada():
    entrada = Tk()
    entrada.title("zolo miyithoz")

    ttk.Label(entrada, text='Ingrese nombre').grid(column=0)
    nombre = StringVar()

    nombre_entry = ttk.Entry(entrada, textvariable=nombre).grid(column=1, row=0)

    ttk.Button(entrada, text='Aceptar', command=aceptar(nombre)).grid(column=2, row=0)


def aceptar(nombre):
    try:
        value = str(nombre.get())
        print(value)
        return value
    except ValueError:
        pass


def menosPeligrosa():
    inicio=input("ingrese inicio ")
    fin=input("ingrese fin ")
    if(grafito.buscarSitio(inicio) != -1 and grafito.buscarSitio(fin) !=-1):

        if(inicio=="la norte" and fin=="aranjuez"):
            panel.create_line(grafito.vertices[0].getX() + 12.5, grafito.vertices[0].getY() + 12.5, grafito.vertices[1].getX() + 12.5, grafito.vertices[1].getY() + 12.5, fill='black')
            panel.update()
        if(inicio=="la norte" and fin=="pereira"):
            panel.create_line(grafito.vertices[0].getX() + 12.5, grafito.vertices[0].getY() + 12.5, grafito.vertices[2].getX() + 12.5, grafito.vertices[2].getY() + 12.5, fill='black')
            panel.update()
        if(inicio=="la norte" and fin=="lab"):
            panel.create_line(grafito.vertices[0].getX() + 12.5, grafito.vertices[0].getY() + 12.5, grafito.vertices[3].getX() + 12.5, grafito.vertices[3].getY() + 12.5, fill='black')
            panel.update()


        if(inicio=="aranjuez" and fin=="la norte"):
            print("destino inacanzable")
        if(inicio=="aranjuez" and fin=="pereira"):
            panel.create_line(grafito.vertices[1].getX() + 12.5, grafito.vertices[1].getY() + 12.5, grafito.vertices[2].getX() + 12.5, grafito.vertices[2].getY() + 12.5, fill='black')
            panel.update()
        if(inicio=="aranjuez" and fin=="lab"):
            print("destino inacanzable")


        if(inicio=="pereira" and fin=="la norte"):
            print("no tengo salidas")
        if(inicio=="pereira" and fin=="aranjuez"):
            print("no tengo salidas")
        if(inicio=="pereira" and fin=="lab"):
            print("no tengo salidas")


        if(inicio=="lab" and fin=="la norte"):
            print("destino innaccesible")
        if(inicio=="lab" and fin=="aranjuez"):
            panel.create_line(grafito.vertices[3].getX() + 12.5, grafito.vertices[3].getY() + 12.5, grafito.vertices[1].getX() + 12.5, grafito.vertices[1].getY() + 12.5, fill='black')
            panel.update()
        if(inicio=="lab" and fin=="pereira"):
            panel.create_line(grafito.vertices[3].getX() + 12.5, grafito.vertices[3].getY() + 12.5, grafito.vertices[2].getX() + 12.5, grafito.vertices[2].getY() + 12.5, fill='black')
            panel.update()
        panel.update()

rutaAnimar=[]

def sugerenciaExperiencia():
    experiencia=input("ingrese su experiencia, alta, media o baja: ")
    if(experiencia=="alta"):
        print("con su alto nivel de experiencia su ruta podría ser: "+grafito.vertices[0].getNombre()+" luego ir a :"+grafito.vertices[1].getNombre()+" terminar su recorrido en: "+grafito.vertices[2].getNombre())
        panel.create_line(grafito.vertices[0].getX() + 12.5, grafito.vertices[0].getY() + 12.5, grafito.vertices[1].getX() + 12.5, grafito.vertices[1].getY() + 12.5, fill='gray')
        rutade0a1a2=[grafito.vertices[0], grafito.vertices[1],grafito.vertices[2]]
        panel.create_line(grafito.vertices[1].getX() + 12.5, grafito.vertices[1].getY() + 12.5, grafito.vertices[2].getX() + 12.5, grafito.vertices[2].getY() + 12.5, fill='gray')
        panel.update()
        rutaAnimar=rutade0a1a2

    if(experiencia=="media"):
        print("con su nivel de experiencia su ruta podría ser: "+grafito.vertices[3].getNombre()+" luego ir a: "+grafito.vertices[2].getNombre()+ " lugar que queda en la misma ciudad ")
        panel.create_line(grafito.vertices[3].getX() + 12.5, grafito.vertices[3].getY() + 12.5, grafito.vertices[2].getX() + 12.5, grafito.vertices[2].getY() + 12.5, fill='gray')
        rutade3a2=[grafito.vertices[3], grafito.vertices[2],grafito.vertices[2]]
        panel.update()
        rutaAnimar=rutade3a2

    if(experiencia=="baja"):
        print("con su nivel de experiencia su ruta podría ser: "+grafito.vertices[0].getNombre()+" luego ir a:"+grafito.vertices[1].getNombre())
        panel.create_line(grafito.vertices[0].getX() + 12.5, grafito.vertices[0].getY() + 12.5, grafito.vertices[1].getX() + 12.5, grafito.vertices[1].getY() + 12.5, fill='gray')
        rutade0a1=[grafito.vertices[0], grafito.vertices[1]]
        panel.update()
        rutaAnimar=rutade0a1
    return rutaAnimar
    panel.update()

def definidir_direccion(nodoinicio,nodofin):
    if grafito.vertices[0].getX() < grafito.vertices[1].getX():
            direccion=0
    elif grafito.vertices[0].getX() == grafito.vertices[1].getX():
            if grafito.vertices[0].getY() > grafito.vertices[1].getY():
                direccion=-1
            else:
                direccion=1
    else:
        direccion=2
    return direccion


def archivo(grafo):
    f = open('file.txt').read()
    lines = f.splitlines()

    for s in lines:
        result = s.split(' ')
        grafo.agregarSitio(result[0])
    for l in lines:
        result = l.split(' ')
        for i in range(0, len(result)-2):
            grafo.agregarCamino(result[0], result[i+1], TRUE)

def animacion():
    ruta=[grafito.vertices[0], grafito.vertices[1],grafito.vertices[2]]
    animar(ruta, True)

def animar(ruta, banderazo):
    nodoinicio=ruta[0]
    nodofin=ruta[1]
    obj=panel.create_oval(nodoinicio.getX(), nodoinicio.getY(),nodoinicio.getX()+20, nodoinicio.getY()+20)
    while banderazo:
        x=5
        y=5
        for i in range(0,len(ruta)-1):
            direccion=definidir_direccion(ruta[i], ruta[i+1])
            print(direccion)
            if direccion==0:
                for i in range(0, 10):

                    time.sleep(0.5)
                    panel.move(obj, x, 0)
                    panel.update()
            if direccion==1:
                for i in range(0,ruta[i+1].getY()):
                    time.sleep(0.5)
                    panel.move(obj,0,y)
                    panel.update()
            if direccion==-1:
                for i in range(0, ruta[i+1].getY()):
                    time.sleep(0.5)
                    panel.move(obj,0,-y)
                    panel.update()
            if direccion==2:
                for i in range(0, ruta[i+1].getX()):
                    time.sleep(0.5)
                    panel.move(obj,-x,0)
                    panel.update()
        banderazo=False

grafito.agregarCamino("la norte", "aranjuez", TRUE)
grafito.agregarCamino("aranjuez", "pereira",  TRUE)
grafito.agregarCamino("la norte", "pereira",  TRUE)
grafito.agregarCamino("la norte","lab",TRUE)
grafito.agregarCamino("lab","pereira", TRUE)
grafito.agregarCamino("lab","aranjuez",TRUE)

g=grafo()

root = Tk()
root.title("CicloRutas Manizales")
casoPintar=IntVar()
casoLineas=IntVar()
CasoEliminar=IntVar()
framePrincipal = ttk.Frame(root, borderwidth="4", relief="groove")
framePrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
framePrincipal.columnconfigure(0, weight=1)
framePrincipal.rowconfigure(0, weight=1)
panel = Canvas(framePrincipal, bg='cyan', width=400, height=400)
botonCargar = ttk.Button(framePrincipal, text="Cargar Grafo", command=cargar_grafo)
botonCargar.grid(column=1, row=0)
botonCrear=ttk.Button(framePrincipal, text="Crear Grafo", command=habilitar)
botonCrear.grid(column=1, row=1)
checkButtonCrear = Checkbutton(framePrincipal, text="Crear Grafo", variable=casoPintar, onvalue=1, offvalue=0, state=DISABLED)
checkButtonCrear.grid(column=1, row=2)
checkButtonCrearlin = Checkbutton(framePrincipal, text="Añadir Lineas", variable=casoLineas, onvalue=1, offvalue=0, state=DISABLED)
checkButtonCrearlin.grid(column=1, row=3)
checkButtonEliminar = Checkbutton(framePrincipal, text="Eliminar", variable=CasoEliminar, onvalue=1, offvalue=0, state=DISABLED)
checkButtonEliminar.grid(column=1, row=4)
botonMenosPeligroso = ttk.Button(framePrincipal, text="Menos Peligrosa", command=menosPeligrosa)
botonMenosPeligroso.grid(column=0, row=1)
botonsugerirExperiencia = ttk.Button(framePrincipal, text="sugerir experiencia", command=sugerenciaExperiencia)
botonsugerirExperiencia.grid(column=0, row=2)

botonAnimar=ttk.Button(framePrincipal, text="Animar", command=animacion)
botonCrear.grid(column=0, row=3)

panel.bind('<Button -1>', funcion_de_funciones)
panel.bind('<Button -3>', eiminar)


for child in framePrincipal.winfo_children(): child.grid_configure(padx=10, pady=10)

root.mainloop()
