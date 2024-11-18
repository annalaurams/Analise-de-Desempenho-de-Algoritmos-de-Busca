import time
from memory_profiler import profile

labirinto = [
    ['A', 'B!?', '!C', 'D?', 'E'],
    ['?F', '?G?', '?H', 'I!?', '?!J'],
    ['K?!', '!L?', 'M?', '?N', '?O?'],
    ['P!', '!Q!', '?!E', '?S?', 'T?'],
    ['U', 'V', 'X?', 'Y?', 'Z']
]

def get_permitted_moves(cell):
    # Inicializa os movimentos permitidos
    moves = {
        "left": [0, -1],
        "right": [0, 1],
        "up": [-1, 0],
        "down": [1, 0]
    }

    # Converte cell em uma lista mutável para manipular os caracteres
    cell_list = list(cell)
    
    while '?' in cell_list or '!' in cell_list:
        if '?' in cell_list:
            index = cell_list.index('?')
            if index == 0:
                moves.pop("down", None)  # '?' na posição 0 significa parede abaixo
            else:
                moves.pop("up", None)    # '?' na posição 1 significa parede acima
            cell_list.pop(index)  # Remove '?' já processado

        if '!' in cell_list:
            index = cell_list.index('!')
            if index == 0:
                moves.pop("left", None)  # '!' na posição 0 significa parede à esquerda
            else:
                moves.pop("right", None) # '!' na posição 1 significa parede à direita
            cell_list.pop(index)  # Remove '!' já processado

    return list(moves.values())

@profile  
def DFS(labirinto, start, end):
    LINHAS, COLUNAS = len(labirinto), len(labirinto[0])
    visitados = set()
    caminho_atual = []
    encontrou_caminho = False

    def dfs_recursive(linha, coluna, caminho):
        nonlocal encontrou_caminho
        
        # Checa se alcançou o ponto de destino
        if (linha, coluna) == end:
            print(f"DFS: Caminho encontrado até {labirinto[end[0]][end[1]]} com caminho: {' -> '.join(caminho)}")
            return True

        # Marca como visitado
        visitados.add((linha, coluna))
        caminho.append(labirinto[linha][coluna])

        # Obtém movimentos permitidos
        movimentos = get_permitted_moves(labirinto[linha][coluna])
        # print(f"DFS: Letra atual: {labirinto[linha][coluna]} | Caminho atual: {' -> '.join(caminho)} | movimentos: {movimentos}")
        # print("\n")
        # Tenta cada movimento na profundidade antes de retroceder
        for auxLinha, auxColuna in movimentos:
            newLinha, newColuna = linha + auxLinha, coluna + auxColuna
            if 0 <= newLinha < LINHAS and 0 <= newColuna < COLUNAS and (newLinha, newColuna) not in visitados:
                if dfs_recursive(newLinha, newColuna, caminho):
                    encontrou_caminho = True
                    break  # Se encontrar o caminho, interrompe a recursão para esta chamada

        # Retrocede removendo a última célula e desmarcando como visitado
        if not encontrou_caminho:
            caminho.pop()
            visitados.remove((linha, coluna))
        return encontrou_caminho

    # Chama a DFS recursiva e exibe o resultado
    encontrou_caminho = dfs_recursive(start[0], start[1], caminho_atual)
    if encontrou_caminho:
        return len(caminho_atual) - 1
    else:
        print("DFS: Destino não alcançável")
        return -1

# Executa a busca DFS
start = (4, 0)
end = (0, 4)

start_time = time.time()
resultado = DFS(labirinto, start, end)
print("\nMenor caminho encontrado pelo DFS:", resultado)

end_time = time.time()
duracao_bfs = (end_time - start_time)  # segundos

print(f"\nTempo de execução:  {duracao_bfs:.4f} segundos")
