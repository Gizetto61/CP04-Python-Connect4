# O jogo começa aqui!

# ===========================
# CONSTANTES DO JOGO
# ===========================

# Linhas e Colunas do tabuleiro são sempre constantes!
LINHAS = 6
COLUNAS = 7
VAZIO = ""

# ===========================
# FUNÇÕES
# ===========================


# ===========================
# VERIFICAR VITÓRIA
# ===========================
def verificar_vitoria(tabuleiro, jogador):

    # Definição das direções
    direcoes = [
        (0, 1),    # Horizontal - A linha não descloca (0) e a coluna desloca para a direita uma casa (1): REPRESENTAÇÃO => -
        (1, 0),    # Vertical - A linha se desloca para baixo uma casa (1) e a coluna não desloca: REPRESENTAÇÃO => |
        (1, 1),    # Diagonal descendente - A linha se desloca para baixo uma casa (1) e a coluna se desloca uma casa para a direita (1): REPRESENTAÇÃO => \
        (1, -1)    # Diagonal ascendente - A linha se desloca para baixo uma casa (1) e a coluna se desloca uma casa para a esquerda (-1): REPRESENTAÇÃO => /
    ]

    # Laço duplo que percorre as 42 posições do tabuleiro da esquerda para a direita e de cima a baixo
    for linha in range(LINHAS):
        for coluna in range(COLUNAS):
            # Verifica se aquela posição pertence ao jogador analizado. Pode ser A, V [Amarelo ou Vermelho] ou VAZIO
            if tabuleiro[linha][coluna] != jogador:
                # Senão pertencer ele pula o laço e analisa a próxima posição
                continue
            # Analisa cada tipo de direção e atribui ao deslocamento da Linha e Coluna
            for deslocamentoLinha, deslocamentoColuna in direcoes: # Primeiro analisa o deslocamento na HORIZONTAL(0, 1), depois na VERTICAL(1, 0), depois na DIAGONAL DESCENDENTE (1, 1), e por último na DIAGONAL ASCENDENTE(1, -1).
                # contador que chega até 4 para avaliar a vitória
                contador = 0
                # Laço que percorre 4 vezes = 4 fichas
                for i in range(4):
                    # Definição da direção do deslocamento da nova posição do tabuleiro
                    # Deslocando a posição
                    nova_linha = linha + i * deslocamentoLinha
                    nova_coluna = coluna + i * deslocamentoColuna
                    # Verificação
                    if (
                        0 <= nova_linha < LINHAS # Se a linha da nova posição verificada estiver dentro do tabuleiro
                        and 0 <= nova_coluna < COLUNAS # Se a coluna da nova posição verificada estiver dentro do tabuleiro
                        and tabuleiro[nova_linha][nova_coluna] == jogador # Se a nova posição verificada for pertencente ao jogador analisado
                    ):
                        # Começa a perceber uma sequência
                        contador += 1

                    else:
                        # Senão quebra o laço e muda a direção redefinido os deslocamentos
                        break

                if contador == 4:
                    # Se o contador chegar a 4 significa que há 4 posições consecutivas em que o jogador analisado colocou as fichas = VITÒRIA
                    return True
    # Se em nenhuma das direções de deslocamento há 4 fichas do mesmo jogador, o jogo continua
    return False

# ===========================
# VERIFICAR EMPATE
# ===========================
def verificar_empate(tabuleiro):
    # Laço que percorre apenas as colunas
    for coluna in range(COLUNAS):
        # Condicional que verifica se há alguma posição na primeira linha do tabuleiro que está vazia
        # Não precisa verificar todo o tabuleiro porque se todas as posições da primeira linha estiverem cheias, logo o tabuleiro inteiro está completo e ninguem venceu por que a função verificar_vitoria() não identificou nenhum vencedor
        if tabuleiro[0][coluna] == VAZIO:
            # Ainda tem jogo! Sem empate
            return False
    # Deu empate
    return True