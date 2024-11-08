import networkx as nx
import matplotlib.pyplot as plt

def carregar_grafo(filename):
    
    G = nx.Graph()
    
    with open(filename, 'r') as file:
        linhas = file.readlines()
        
        colunas = linhas[0].strip().split(',')[1:]  # Ignorar primeiro elemeiten (vazio)

        G.add_nodes_from(colunas)
        
        for i, linha in enumerate(linhas[1:]):
            dados = linha.strip().split(',')
            nodo = dados[0]
            for j, valor in enumerate(dados[1:]):
                if valor == '1':
                    G.add_edge(nodo, colunas[j])
                    #print(f"Aresta entre {nodo} e {colunas[j]}")  # Verificação

    return G

# Carrega o grafo do arquivo
G = carregar_grafo('Maze.csv')

# Mostra o grafo
# plt.figure(figsize=(10, 8))
# nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', font_weight='bold')
# plt.title("Grafo")
# plt.show()
