from collections import deque

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

    # Inicializa fila_letras como uma lista vazia
    fila_letras = []

    while fila:
        (linha, coluna), comprimento = fila.popleft()
        
        # Mostra a célula atual e o comprimento até o momento
        print(f"BFS: Letra atual: {labirinto[linha][coluna]} com comprimento atual: {comprimento}")

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
        print(f"Fila: {fila_letras}")
        print("\n")

    print("BFS: Destino não alcançável")
    return -1  # Caso o destino não seja alcançável

# Executa a busca BFS
start = (4, 0)
end = (2, 1)
resultado = BFS(labirinto, start, end)
print("\nMenor caminho encontrado pelo BFS:", resultado)

