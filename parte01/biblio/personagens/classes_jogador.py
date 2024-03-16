#Definição de classes
class Personagem:
    def __init__(self, nome:str, vida:int, ataque:int) -> None:
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.vivo = True
        self.localizacao = 'inicio'
    
    def check_status(self) -> None:
        print(f'Nome: {self.nome}\n'
              f'Vida: {self.vida}/{self.vidamax}\n'
              f'Ataque: {self.ataque}')
    
    def atacar(self, inimigo) -> None:
        if inimigo.vida - self.ataque <= 0:
            inimigo.vivo = False
            inimigo.vida = 0
        else:
            inimigo.vida -= self.ataque

class Arqueiro(Personagem):
    def __init__(self, nome: str) -> None:
        super().__init__(nome, vida=20, ataque=3)
    
    def check_status(self) -> None:
        print('Você aponta o seu arco e atira')
        super().check_status()

if __name__ == '__main__':
    le = Arqueiro('LEt')
    print(le.localizacao)