from collections import defaultdict 

class Grafo: 
  
    def __init__(self): # criando o grafo       
        self.grafo = defaultdict(list) # lista default para grafo
  
    def addAresta(self, u, v): # função para add vértice
        self.grafo[u].append(v) 
    
    def BFS(self, s): # função de busca em largura           
        visitado = [False] * (len(self.grafo)) # marca todos os vertices como não visitados
        fila = [] # cria fila para a BFS
  
        fila.append(s) # add o vertice na fila
        visitado[s] = True # marca como visitado
  
        while fila: 
            s = fila.pop(0) # tiro o vertice da fila
            print (s, end = " ") # printo o vertice

            for i in self.grafo[s]: # de todos os vertices adjacentes
                if visitado[i] == False: # se não foi visitado ainda
                    fila.append(i) # coloco na fila
                    visitado[i] = True # marco como visitado
    
    def DFS2(self, v, visitado): # função recursiva de busca em profundidade
        visitado[v]= True # marca o vertice como visitado
        print (v, end = " ") # printo o vertice
  
        for i in self.grafo[v]: # para cada vertice adjacente
            if visitado[i] == False: # se não foi visitado ainda
                self.DFS2(i, visitado) # recursivo nele
  
    def DFS(self): 
        total = len(self.grafo)  # total de vertices  
        visitado =[False]*(total) # marca todos os vertices como nao visitado

        for i in range(total): 
            if visitado[i] == False: # se nao foi visitado ainda
                self.DFS2(i, visitado) # executa busca nele
  
# main:
g = Grafo() 

qtd_arestas = int(input("Qtd de arestas: "))
print ("Digite as arestas (u v):")
i = 0
while i < qtd_arestas:
    aresta1, aresta2 = input().split(" ")
    aresta1 = int(aresta1)
    aresta2 = int(aresta2)
    g.addAresta(aresta1, aresta2)
    i = i+1

inicial = int(input("Aresta que deseja começar: "))
print ("BFS: ", end = "")
g.BFS(inicial)
print ("\nDFS: ", end = "")
g.DFS() 