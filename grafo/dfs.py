from grafo import G  
import time
from memory_profiler import profile

#@profile  
def dfs_rec(adj, visited, s, fim):

    visited[s] = True

    print(s, end=" ")
    print("")

    if s == fim:
        
        print(f"\nFim da busca encontrado em: {s}\n")
        return True

    for i in adj[s]:
        if not visited[i]:
            if dfs_rec(adj, visited, i, fim):  
                return True

    print(f"Desempilhando: {s}")
    return False

@profile  
def dfs(adj, inicio, fim):
    visited = {key: False for key in adj}  
  
    if not dfs_rec(adj, visited, inicio, fim):
        print(f"\nO vértice de destino '{fim}' não foi encontrado no grafo.")


inicio = 'U'  
fim = 'A'    
print("Iniciando DFS:")

start_time = time.time() 
dfs(G, inicio, fim)
end_time = time.time()

duracao_bfs = (end_time - start_time)  

print(f"\nTempo de execução: {duracao_bfs:.4f} segundos\n")

