from collections import deque
from grafo import G
import networkx as nx
import time
from memory_profiler import profile

@profile  
def bfs(G, inicio, fim):
    visitados = set()
    fila = deque([inicio])
    
    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            print(vertice, end=' ')
            print("")
            visitados.add(vertice)
            
            if vertice == fim:
                print("\nFim da busca.\n")
                return
        
            fila.extend(set(G[vertice]) - visitados)

    print("\nO vértice de destino não foi encontrado no grafo.")

inicio = 'U'  
fim = 'A'     
start_time = time.time()
bfs(G, inicio, fim)
end_time = time.time()
duracao_bfs = (end_time - start_time)  

print(f"\nTempo de execução:  {duracao_bfs:.4f} segundos \n")
