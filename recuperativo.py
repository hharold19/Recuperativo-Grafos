# Grafo - nodos enlazados -
# Autor: Javier Rivera
# Colaboradores: Harold Hernandez, Meleyca Cabrera
# ver: https://repl.it/EdpH/0

class Nodo:
    def __init__ (self, valor):
        self.info = valor
        self.arcos = []
        
    def enlace (self, ndestino, peso = 1, bdir = False):
        if (type(ndestino) == type(self)):
            arco = Arco(ndestino, peso)
            self.arcos.append(arco)
            if (bdir == True):
                arco = Arco(self, peso)
                ndestino.arcos.append(arco)
            return True
        return False
        
    def muestra_enlaces (self):
        for arco in self.arcos: 
            print arco.nodo.info,
            print arco.peso
            
    def existe_enlace(self, ndestino):
        for arco in self.arcos:
            if (arco.nodo == ndestino):
                return arco
        return False
    def existe_enlace_peso(self, ndestino):
        for arco in self.arcos:
            if (arco.nodo == ndestino):
                return arco
        return False
        
    def eli_enlace (self, ndestino):
        arco = self.existe_enlace(ndestino)
        if (arco != False):
            self.arcos.remove(arco)
            return True
        return False
            
    def __del__(self):
        del self.arcos
        
class Arco:
    def __init__ (self, ndestino, peso=0):
        self.nodo = ndestino
        self.peso = peso
class Arista:
    def __init__ (self,norigen, ndestino, peso=0):
        self.origen = norigen
        self.nodo = ndestino
        self.peso = peso

class Grafo:
    def __init__(self, dirigido = True):
        self.__nodos = []
        self.__dirigido = dirigido
        
    def buscaNodo (self, valor):
        for nodo in self.__nodos:
            if (nodo.info == valor):
                return nodo
        return False
    
    def enlace(self, valOrigen, valDestino, peso = 1, bdir = False):
        
        norigen = self.buscaNodo(valOrigen)
        if (not(norigen)):
            return False
            
        ndestino = self.buscaNodo(valDestino)
        if (not(ndestino)):
            return False
        
        if (self.__dirigido == False):
            bdir = True
            
        norigen.enlace(ndestino, peso, bdir)
        return True

    # metodo insetar para el grafo orginal	
    def ins_nodo (self, valor):
        if (self.buscaNodo(valor) == False):
            nodo = Nodo(valor)
            self.__nodos.append(nodo)
            return nodo
        return False
        
    def __str__(self):
        grafo  = ""
        for nodo in self.__nodos:
            grafo = grafo + nodo.info
            arcos = ""
            for arco in nodo.arcos:
                if (arcos != ""):
                    arcos = arcos + ", "
                arcos = arcos + arco.nodo.info + ":" + str(arco.peso)
            grafo = grafo + "(" + arcos + ") "
        return grafo
        
    # Metodo muestra el peso y la arista que mayor valor en un camino solicitado
    def arista_mayor_peso(self, nOrigen , nDestino, inic=True):
      
        if (inic == True):
            self.__listaC = []
            self.__otra_lista = Arista( None, None, 0) 
        self.__listaC.append(nOrigen.info)
        existeArco = nOrigen.existe_enlace(nDestino)
        
        if (existeArco):
            self.__listaC.append(nDestino.info)
            if(self.__otra_lista.peso < existeArco.peso):
                self.__otra_lista.peso = existeArco.peso
                self.__otra_lista.origen = nOrigen.info
                self.__otra_lista.ndestino = nDestino.info
            return self.__otra_lista.peso,self.__otra_lista.origen,self.__otra_lista.ndestino

        for arco in nOrigen.arcos:
            
            if (arco.nodo.info in self.__listaC):
                continue
            encuentra = self.arista_mayor_peso(arco.nodo,nDestino,False)
            
            if (encuentra):
                if (self.__otra_lista.peso < arco.peso):
                    self.__otra_lista.peso = arco.peso
                    self.__otra_lista.origen = nOrigen.info
                    self.__otra_lista.ndestino = arco.nodo.info				
                return self.__otra_lista.peso,self.__otra_lista.origen,self.__otra_lista.ndestino

            self.__listaC.pop(len(self.__listaC)-1)

        return False



# Principal

g = Grafo()
nodo1 = g.ins_nodo("A")
nodo2 = g.ins_nodo("B")
nodo3 = g.ins_nodo("C")
nodo4 = g.ins_nodo("D")
nodo5 = g.ins_nodo("E")
nodo6 = g.ins_nodo("F")

nodo1.enlace(nodo2,1)		
nodo2.enlace(nodo3,5)
nodo3.enlace(nodo4,6)
nodo1.enlace(nodo5,3)
nodo5.enlace(nodo6,2)

# Prueba del camino entre nodo A hasta nodo F
print "Arista Mayor entre nodo A y nodo F"
print g.arista_mayor_peso(nodo1,nodo6)

# Prueba del camino entre nodo A hasta nodo D
print "Arista Mayor entre nodo A y nodo D"
print g.arista_mayor_peso(nodo1,nodo4)

# Prueba del camino entre nodo B hasta nodo D
print "Arista Mayor entre nodo B y nodo D"
print g.arista_mayor_peso(nodo2,nodo4)

# Prueba del camino entre nodo B hasta nodo E
print "Arista Mayor entre nodo B y nodo E"
print g.arista_mayor_peso(nodo2,nodo5)
