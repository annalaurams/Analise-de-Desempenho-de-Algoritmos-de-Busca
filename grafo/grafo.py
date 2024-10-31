import networkx as nx
import matplotlib.pyplot as plt

# Leitura do arquivo e criação do grafo
def carregar_grafo(filename):
    # Cria um grafo vazio
    G = nx.Graph()
    
    # Abre o arquivo e lê linha por linha
    with open(filename, 'r') as file:
        linhas = file.readlines()
        
        
        # A primeira linha contém os rótulos das colunas
        colunas = linhas[0].strip().split(',')[1:]  # Ignora o primeiro elemento vazio

        # Adiciona os nós ao grafo
        G.add_nodes_from(colunas)
        
        # Itera sobre as linhas para adicionar arestas
        for i, linha in enumerate(linhas[1:]):
            dados = linha.strip().split(',')
            nodo = dados[0]
            for j, valor in enumerate(dados[1:]):
                if valor == '1':
                    # Adiciona uma aresta se houver conexão (valor == 1)
                    G.add_edge(nodo, colunas[j])
                    #print(f"Aresta adicionada entre {nodo} e {colunas[j]}")  # Verificação

    return G

# Carrega o grafo do arquivo
G = carregar_grafo('Maze.csv')




# # Exibe o grafo
# plt.figure(figsize=(10, 8))
# nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', font_weight='bold')
# plt.title("Grafo a partir da Matriz de Adjacência")
# plt.show()
