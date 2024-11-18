from collections import deque
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
def BFS(labirinto, start, end):
    
    LINHAS, COLUNAS = len(labirinto), len(labirinto[0])
    visitados = set()
    fila = deque([(start, 0)])  # Inclui o comprimento inicial
    visitados.add(start)

    # Inicializa fila_letras como uma lista vazia
    fila_letras = []

    while fila:
        (linha, coluna), comprimento = fila.popleft()
        
        # Mostra a célula atual e o comprimento até o momento
        # print(f"BFS: Letra atual: {labirinto[linha][coluna]} com comprimento atual: {comprimento}")

        # Checa se alcançou o ponto de destino
        if (linha, coluna) == end:
            print(f"BFS: Caminho encontrado até {labirinto[end[0]][end[1]]} com comprimento: {comprimento}")
            return comprimento
        
        # Obtém movimentos permitidos
        movimentos = get_permitted_moves(labirinto[linha][coluna])

        # Itera sobre movimentos, mostrando letras nas células
        for auxLinha, auxColuna in movimentos:
            newLinha, newColuna = linha + auxLinha, coluna + auxColuna
            if 0 <= newLinha < LINHAS and 0 <= newColuna < COLUNAS and (newLinha, newColuna) not in visitados:
                fila.append(((newLinha, newColuna), comprimento + 1))
                # Adiciona a letra correspondente à fila_letras
                fila_letras.append(labirinto[newLinha][newColuna])  # Adiciona a letra da nova posição
                visitados.add((newLinha, newColuna))

        # Exibe a fila com letras, não coordenadas
        # print(f"Fila: {fila_letras}")
        # print("\n")

    print("BFS: Destino não alcançável")
    return -1  # Caso o destino não seja alcançável

# Executa a busca BFS
start = (4, 0)
end = (0, 4)
resultado = BFS(labirinto, start, end)

start_time = time.time()
print("\nMenor caminho encontrado pelo BFS:", resultado)
end_time = time.time()
duracao_bfs = (end_time - start_time) #segundos

print(f"\nTempo de execução:  {duracao_bfs:.4f} segundos")

