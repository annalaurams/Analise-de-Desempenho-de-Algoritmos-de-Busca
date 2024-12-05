import networkx as nx
from grafo2 import G  
import time
from memory_profiler import profile

# Tabela hash - heurística
heuristica = {
    'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0,
    'F': 5, 'G': 4, 'H': 3, 'I': 2, 'J': 1,
    'K': 6, 'L': 5, 'M': 4, 'N': 3, 'O': 2,
    'P': 7, 'Q': 6, 'R': 5, 'S': 4, 'T': 3,
    'U': 8, 'V': 2, 'X': 6, 'Y': 5, 'Z': 4
}

@profile  
def algoritmo_guloso(grafo, heuristica, origem, destino):
   
    caminho = [origem] 
    visitados = set() 
    atual = origem
    print(f"Início: {atual}")

    while atual != destino:
        visitados.add(atual) 
        
        vizinhos = [nodo for nodo in grafo.neighbors(atual) if nodo not in visitados]

        if not vizinhos:
            print("Caminho impossível!")
            return []

        proximo = min(
            vizinhos, 
            key=lambda nodo: (heuristica[nodo], nodo) 
        )

        print(f"De {atual} para {proximo} (heurística: {heuristica[proximo]})")
        caminho.append(proximo)
        atual = proximo

    print(f"Caminho completo: {caminho}")
    return caminho


if __name__ == "__main__":
    
    origem = 'U'  
    destino = 'E' 

    start_time = time.time()
    
    caminho = algoritmo_guloso(G, heuristica, origem, destino)
    
    end_time = time.time()

    duracao_bfs = (end_time - start_time)  

    print(f"\nTempo de execução: {duracao_bfs:.4f} segundos\n")
