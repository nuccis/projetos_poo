from random import randint
from math import trunc
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
              f'Ataque: {self.ataque}\n')
    
    def atacar(self, jogador) -> None:
        dano = randint(trunc(self.ataque*0.6), self.ataque)
        if jogador.vida - dano <= 0:
            jogador.vivo = False
            jogador.vida = 0
        else:
            jogador.vida -= dano
            print(f'Infligindo {dano} de dano à você') 
    
    def status(self):
        #aqui irá retornar textos para diferentes status do inimigo: vivo, ferido e morto
        if self.vida == self.vidamax:
            print(f'O {self.nome} te encara friamente')
        elif self.vida > 0 and self.vida < self.vidamax:
            print(f'O {self.nome} está com marcas de sangue pelo corpo')
            print(f'Vida do {self.nome}: {self.vida}/{self.vidamax}')
        else:
            print(f'O {self.nome} jaz imóvel sem vida no chão')
            print(f'Vida do {self.nome}: {self.vida}/{self.vidamax}')


        
class Lobo(InimigoBasico):
    def __init__(self, nome: str, vida: int, ataque: int) -> None:
        super().__init__(nome, vida, ataque)
    
    def atacar(self, jogador) -> None:
        print('O lobo rosna e ataca')      
        super().atacar(jogador)

class Urso(InimigoBasico):
    def __init__(self, nome: str, vida: int, ataque: int) -> None:
        super().__init__(nome, vida, ataque)
    
    def atacar(self, jogador) -> None:
        print('O urso ruge e ataca')
        super().atacar(jogador)

class Draco(InimigoBasico):
    def __init__(self, nome: str, vida: int, ataque: int) -> None:
        super().__init__(nome, vida, ataque)
    
    def atacar(self, jogador) -> None:
        print('O draco irrompe em chamas e ataca')      
        return super().atacar(jogador)