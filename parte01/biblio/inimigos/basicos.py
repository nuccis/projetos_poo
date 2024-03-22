#Definição de classes
class InimigoBasico:
    def __init__(self, nome:str, vida:int, ataque:int) -> None:
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.vivo = True
    
    def __str__(self) -> str:
        return(f'Nome: {self.nome}\n'
              f'Vida: {self.vida}/{self.vidamax}\n'
              f'Ataque: {self.ataque}')
    
    def atacar(self, jogador) -> None:
        if jogador.vida - self.ataque <= 0:
            jogador.vivo = False
            jogador.vida = 0
        else:
            jogador.vida -= self.ataque
    
    def status(self):
        #aqui irá retornar textos para diferentes status do lobo: vivo, ferido e morto
        pass

class Lobo(InimigoBasico):
    def __init__(self, nome, vida, ataque) -> None:
        super().__init__(nome, vida, ataque)
    
    def atacar(self, jogador) -> None:
        print('O lobo rosna e ataca')
        super().atacar(jogador)

class Urso(InimigoBasico):
    def __init__(self, nome, vida, ataque) -> None:
        super().__init__(nome, vida, ataque)
    
    def atacar(self, jogador) -> None:
        print('O urso ruge e ataca')
        super().atacar(jogador)