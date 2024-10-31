# from grafo import G  # Importando o grafo G do módulo grafo
# import time

# def dfs_rec(adj, visited, s, fim):
#     # Marca o vértice atual como visitado
#     visited[s] = True

#     # Imprime o vértice atual
#     print(s, end=" ")

#     # Se o vértice atual é o fim, finalize a busca
#     if s == fim:
#         print(f"\nFim da busca encontrado em: {s}")
#         return True

#     # Visita recursivamente todos os vértices adjacentes
#     # que ainda não foram visitados
#     for i in adj[s]:
#         if not visited[i]:
#             if dfs_rec(adj, visited, i, fim):  # Passa o fim para as chamadas recursivas
#                 return True

#     # Imprime o vértice ao "desempilhar"
#     print(f"Desempilhando: {s}")
#     return False

# def dfs(adj, inicio, fim):
#     visited = {key: False for key in adj}  # Usando um dicionário para rastrear visitados
#     # Chama a função recursiva DFS
#     if not dfs_rec(adj, visited, inicio, fim):
#         print(f"\nO vértice de destino '{fim}' não foi encontrado no grafo.")

# # Executar a DFS
# inicio = 'U'  # Vértice de início
# fim = 'E'     # Vértice de fim
# print("Iniciando DFS:")
# start_time = time.time()
# dfs(G, inicio, fim)
# end_time = time.time()
# duracao_bfs = (end_time - start_time) * 1e6  # Microssegundos

# print(f"\nTempo de execução:  {duracao_bfs:.4f} microsegundos")

from grafo import G  # Importando o grafo G do módulo grafo
import time
from memory_profiler import profile

@profile  # Adiciona o decorador para monitorar a função
def dfs_rec(adj, visited, s, fim):
    # Marca o vértice atual como visitado
    visited[s] = True

    # Imprime o vértice atual
    print(s, end=" ")

    # Se o vértice atual é o fim, finalize a busca
    if s == fim:
        print(f"\nFim da busca encontrado em: {s}")
        return True

    # Visita recursivamente todos os vértices adjacentes
    # que ainda não foram visitados
    for i in adj[s]:
        if not visited[i]:
            if dfs_rec(adj, visited, i, fim):  # Passa o fim para as chamadas recursivas
                return True

    # Imprime o vértice ao "desempilhar"
    print(f"Desempilhando: {s}")
    return False

#@profile  # Adiciona o decorador para monitorar a função
def dfs(adj, inicio, fim):
    visited = {key: False for key in adj}  # Usando um dicionário para rastrear visitados
    # Chama a função recursiva DFS
    if not dfs_rec(adj, visited, inicio, fim):
        print(f"\nO vértice de destino '{fim}' não foi encontrado no grafo.")

# Executar a DFS
inicio = 'U'  # Vértice de início
fim = 'E'     # Vértice de fim
print("Iniciando DFS:")

start_time = time.time()  # Captura o tempo inicial
dfs(G, inicio, fim)
end_time = time.time()

duracao_bfs = (end_time - start_time) * 1e6  # Microssegundos

print(f"\nTempo de execução: {duracao_bfs:.4f} microsegundos")

