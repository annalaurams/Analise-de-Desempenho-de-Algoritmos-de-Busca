import networkx as nx
from grafo2 import G  # Importa o grafo definido como 'G'
import time
from memory_profiler import profile

# Tabela hash para representar a heurística
heuristica = {
    'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0,
    'F': 5, 'G': 4, 'H': 3, 'I': 2, 'J': 1,
    'K': 6, 'L': 5, 'M': 4, 'N': 3, 'O': 2,
    'P': 7, 'Q': 6, 'R': 5, 'S': 4, 'T': 3,
    'U': 8, 'V': 7, 'X': 6, 'Y': 5, 'Z': 4
}

@profile  
def algoritmo_a_estrela(grafo, heuristica, origem, destino):
 
    # Inicialização das estruturas
    caminho = []  # Armazena o caminho final
    visitados = set()  # Conjunto de nós já explorados
    fila = [(0 + heuristica[origem], 0, origem, [])]  # (f, g, nó_atual, caminho_antes)

    while fila:
        # Ordena a fila com base no menor valor de f = g + h
        fila.sort(key=lambda x: x[0])
        f_atual, g_atual, atual, caminho_atual = fila.pop(0)

        if atual in visitados:
            continue

        caminho = caminho_atual + [atual]
        visitados.add(atual)

        # Imprime o estado atual
        print(f"\nExplorando nó: {atual}")
        print(f"  g (custo acumulado): {g_atual}")
        print(f"  h (heurística): {heuristica[atual]}")
        print(f"  f (g + h): {f_atual}")

        # Verifica se o destino foi alcançado
        if atual == destino:
            print(f"\nCaminho encontrado: {caminho}")
            return caminho

        # Explora os vizinhos do nó atual
        for vizinho in grafo.neighbors(atual):
            if vizinho not in visitados:
                custo_g = g_atual + grafo[atual][vizinho].get('weight', 1)  # Custo acumulado (g)
                custo_f = custo_g + heuristica[vizinho]  # f = g + h

                # Imprime os valores do vizinho sendo avaliado
                print(f"  Avaliando vizinho: {vizinho}")
                print(f"    g (custo acumulado): {custo_g}")
                print(f"    h (heurística): {heuristica[vizinho]}")
                print(f"    f (g + h): {custo_f}")

                fila.append((custo_f, custo_g, vizinho, caminho))

    print("\nCaminho impossível!")
    return []


# Exemplo de uso
if __name__ == "__main__":
    origem = 'U'  # Nó inicial
    destino = 'E'  # Nó final

    # Adicionar pesos ao grafo (caso necessário)
    # Exemplo: G.add_edge('U', 'V', weight=1)
    start_time=time.time()
    caminho = algoritmo_a_estrela(G, heuristica, origem, destino)
    end_time = time.time()

    duracao_bfs = (end_time - start_time)  

    print(f"\nTempo de execução: {duracao_bfs:.4f} segundos\n")

