from collections import defaultdict 
import sys 
  
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
  
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    def swapMinHeapNode(self,a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2*idx + 1
        right = 2*idx + 2
  
        if left < self.size and self.array[left][1] < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min  
        # heap if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    def extractMin(self):   
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
        # Get the index of v in  heap array 
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is  
        # not hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[int((i - 1) / 2)][1]: 
  
            # Swap this node with its parent 
            self.pos[self.array[i][0]] = int((i-1)/2)
            self.pos[self.array[int((i-1)/2)][0]] = i 
            self.swapMinHeapNode(i, int((i - 1)/2))
  
            # move to parent index 
            i = (i - 1) / 2 
            i = int(i)
  
    def isInMinHeap(self, v): 
        if self.pos[v] <= self.size: 
            return True
        return False
   
def printArr(dist, n): 
    print ("Vertex\tDistance from source")
    for i in range(n): 
        print ("%d\t\t%d" % (i,dist[i]))
   
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
  
    # Adds an edge to an undirected graph 
    def addEdge(self, src, dest, weight): 
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode)
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 
  
    def dijkstra(self, src): 
        V = self.V  # Get the number of vertices in graph 
        dist = []   # dist values used to pick minimum  
                    # weight edge in cut 
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        #  Initialize min heap with all vertices.  
        # dist value of all vertices 
        for v in range(V): 
            dist.append(sys.maxsize) 
            minHeap.array.append(minHeap.newMinHeapNode(v, dist[v])) 
            minHeap.pos.append(v) 
  
        # Make dist value of src vertex as 0 so  
        # that it is extracted first 
        minHeap.pos[src] = src 
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src]) 
  
        # Initially size of min heap is equal to V 
        minHeap.size = V; 
  
        # In the following loop, min heap contains all nodes 
        # whose shortest distance is not yet finalized. 
        while minHeap.isEmpty() == False: 
  
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
  
            # Traverse through all adjacent vertices of  
            # u (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 
  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less  
                # than its previously calculated distance 
                if minHeap.isInMinHeap(v) and dist[u] != sys.maxsize and pCrawl[1] + dist[u] < dist[v]: 
                        dist[v] = pCrawl[1] + dist[u] 
  
                        # update distance value  
                        # in min heap also 
                        minHeap.decreaseKey(v, dist[v]) 
  
        printArr(dist,V) 
 
# main

print ("Qtd de vertices: ", end = "")
tam = input()
tam = int(tam)
g = Graph(tam)
print ("Qtd de interações: ", end = "")
interacoes = input()

print ("Digite as interações:")
i = 0
while i < interacoes:
    print("a1 a2: ", end ="")
    a1, a2 = input().split(" ")
    print("peso: ", end = "")
    peso = input()
    g.addEdge(a1, a2, peso)

print("Vertice inicial :", end = "")
inicial = input()
g.dijkstra(inicial)