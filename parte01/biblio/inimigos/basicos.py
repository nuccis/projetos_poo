#Definição de classes
class InimigoBasico:
    def __init__(self, nome:str, vida:int, ataque:int) -> None:
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.vivo = True
    
    def check_status(self) -> None:
        print(f'Nome: {self.nome}\n'
              f'Vida: {self.vida}/{self.vidamax}\n'
              f'Ataque: {self.ataque}')
    
    def atacar(self, jogador) -> None:
        if jogador.vida - self.ataque <= 0:
            jogador.vivo = False
            jogador.vida = 0
        else:
            jogador.vida -= self.ataque

class Lobo(InimigoBasico):
    def __init__(self) -> None:
        super().__init__(nome='Lobo', vida=10, ataque=2)
    
    def atacar(self, jogador) -> None:
        print('O lobo rosna e ataca')
        super().atacar(jogador)

class Urso(InimigoBasico):
    def __init__(self) -> None:
        super().__init__(nome='Urso', vida=14, ataque=3)
    
    def atacar(self, jogador) -> None:
        print('O urso ruge e ataca')
        super().atacar(jogador)