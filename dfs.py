# from typing import set
from collections import deque
from queue import Queue
from typing import List, Dict, Tuple

labirinto = [
    ['A', 'B!?', '!C', 'D?', 'E'],
    ['?F', '?G', '?H', 'I!?', '?!J'],
    ['K?!', '!L?', 'M?', '?N', '?O?'],
    ['P!', '!Q!', '?!E', '?S?', 'T?'],
    ['U', 'V', 'X?', 'Y?', 'Z']
]

def get_permitted_moves(cell):
    moves = {
        "left": [0, -1],
        "right": [0, 1],
        "up": [-1, 0],
        "down": [1, 0]
    }
    
    for i, char in enumerate(cell):
        if char == '?':
            if i == 0:
                moves.pop("down", None)  # parede abaixo
            else:
                moves.pop("up", None)    # parede acima
        elif char == '!':
            if i == 0:
                moves.pop("left", None)  # parede na esquerda
            else:
                moves.pop("right", None) # parede na direita
                
    return list(moves.values())


def BFS(labirinto, start, end):
    LINHAS, COLUNAS = len(labirinto), len(labirinto[0])
    visitados = set()
    fila = deque([(start, 0)])  # Inclui o comprimento inicial
    visitados.add(start)

    while fila:
        (linha, coluna), comprimento = fila.popleft()
        
        # Mostra a célula atual e o comprimento até o momento
        print(f"BFS:     ({linha}, {coluna}) com comprimento atual: {comprimento}")

        # Checa se alcançou o ponto de destino
        if (linha, coluna) == end:
            print(f"BFS: Caminho encontrado até {end} com comprimento: {comprimento}")
            return comprimento
        
        # Obtém movimentos permitidos
        movimentos = get_permitted_moves(labirinto[linha][coluna])

        print(f"Movimentos: {movimentos}")
        print(f"Letra:  {labirinto[linha][coluna]}")
        
        
        for auxLinha, auxColuna in movimentos:
            newLinha, newColuna = linha + auxLinha, coluna + auxColuna
            if 0 <= newLinha < LINHAS and 0 <= newColuna < COLUNAS and (newLinha, newColuna) not in visitados:
                fila.append(((newLinha, newColuna), comprimento + 1))
                visitados.add((newLinha, newColuna))
        
            print(f"Fila: {list(fila)}")
    
        print("\n")
    print("BFS: Destino não alcançável")
    return -1  # Caso o destino não seja alcançável

# Executa a busca BFS
start = (4, 0)
end = (0, 4)
resultado = BFS(labirinto, start, end)
print("\nMenor caminho encontrado pelo BFS:", resultado)



def DFS(labirinto, linha, coluna, visitados, end, comprimento=0):
    LINHAS, COLUNAS = len(labirinto), len(labirinto[0])
    
    # Verifica se a célula está fora dos limites, já foi visitada ou é uma parede
    if (linha < 0 or linha >= LINHAS or 
        coluna < 0 or coluna >= COLUNAS or 
        (linha, coluna) in visitados or 
        ('!' in labirinto[linha][coluna] and labirinto[linha][coluna].index('!') == 0 and coluna == 0) or
        ('?' in labirinto[linha][coluna] and labirinto[linha][coluna].index('?') == 0 and linha == LINHAS - 1)):
        return 0

    # Mostra a célula atual e o comprimento até o momento
    print(f"DFS Visitando célula: ({linha}, {coluna}) com comprimento atual: {comprimento}")

    # Verifica se chegou ao ponto final
    if (linha, coluna) == end:
        print(f"DFS: Caminho encontrado até {end} com comprimento: {comprimento}")
        return 1

    visitados.add((linha, coluna))

    caminhos = 0
    movimentos = get_permitted_moves(labirinto[linha][coluna])
    for auxLinha, auxColuna in movimentos:
        newLinha, newColuna = linha + auxLinha, coluna + auxColuna
        caminhos += DFS(labirinto, newLinha, newColuna, visitados, end, comprimento + 1)

    visitados.remove((linha, coluna))
    return caminhos




# Executa a busca DFS
visitados = set()
#resultado = DFS(labirinto, start[0], start[1], visitados, end)
#print("Número de caminhos encontrados pelo DFS:", resultado)