from collections import deque
from grafo import G
import networkx as nx
import time
from memory_profiler import profile

@profile  # Adiciona o decorador para monitorar a função
def bfs(G, inicio, fim):
    visitados = set()
    fila = deque([inicio])
    
    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            print(vertice, end=' ')
            visitados.add(vertice)
            
            # Se o vértice atual é o fim, finalize a busca
            if vertice == fim:
                print("\nFim da busca.")
                return
            
            # Converte G[vertice] para um conjunto para usar a operação de subtração
            fila.extend(set(G[vertice]) - visitados)

    print("\nO vértice de destino não foi encontrado no grafo.")

# Executar o BFS
inicio = 'U'  # Vértice de início
fim = 'E'     # Vértice de fim
start_time = time.time()
bfs(G, inicio, fim)
end_time = time.time()
duracao_bfs = (end_time - start_time) * 1e6  # Microssegundos

print(f"\nTempo de execução:  {duracao_bfs:.4f} microsegundos")
