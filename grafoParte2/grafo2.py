import networkx as nx
import matplotlib.pyplot as plt

def carregar_grafo_com_pesos(filename):
    G = nx.Graph()
    
    with open(filename, 'r') as file:
        linhas = file.readlines()
        
        colunas = linhas[0].strip().split(',')[1:]  # Ignorar primeiro elemento (vazio)

        G.add_nodes_from(colunas)
        
        for i, linha in enumerate(linhas[1:]):
            dados = linha.strip().split(',')
            nodo = dados[0]
            for j, valor in enumerate(dados[1:]):
                if valor != '0':  # Considera apenas conexões com peso
                    peso = float(valor)  # Convertendo o peso para float
                    G.add_edge(nodo, colunas[j], weight=peso)

    return G

# Carrega o grafo do arquivo com pesos
G = carregar_grafo_com_pesos('matriz.csv')

# Mostra o grafo com pesos
# pos = nx.spring_layout(G)
# edge_labels = nx.get_edge_attributes(G, 'weight')  # Obtém os pesos das arestas
# plt.figure(figsize=(10, 8))
# nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', font_weight='bold')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# plt.title("Grafo com Pesos")
# plt.show()
