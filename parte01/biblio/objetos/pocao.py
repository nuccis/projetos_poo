class PocaoVida:
    def __init__(self, nome, valor, descricao) -> None:
        self.nome = nome
        self.valor = valor
        self.descricao = descricao

    
    def usar(self, jogador):
        if jogador.vida + self.valor > jogador.vidamax:
            jogador.vida = jogador.vidamax
        else:
            jogador.vida += self.valor