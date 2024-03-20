#Definição de classes
class Personagem:
    def __init__(self, nome:str, vida:int, ataque:int, localizacao:object) -> None:
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.vivo = True
        self.localizacao = localizacao
    
    def __str__(self) -> str:
        return(f'Nome: {self.nome}\n'
              f'Vida: {self.vida}/{self.vidamax}\n'
              f'Ataque: {self.ataque}\n'
              f'Localização: {self.localizacao}'
              )
    
    def atacar(self, inimigo) -> None:
        if inimigo.vida - self.ataque <= 0:
            inimigo.vivo = False
            inimigo.vida = 0
        else:
            inimigo.vida -= self.ataque
    
    def movimentar(self, mapa:dict):
        print('Caminhos disponíveis:')
        for i, e in enumerate(mapa[self.localizacao.nome]):
            print(f'[{i+1}] {e.nome.capitalize()}')
        resp = int(input('Digite a sua escolha: '))
        self.localizacao = mapa[self.localizacao.nome][resp - 1]


class Arqueiro(Personagem):
    def __init__(self, nome: str, localizacao: object) -> None:
        super().__init__(nome, 20, 3, localizacao)
    
    def atacar(self) -> None:
        print('Você aponta o seu arco e atira')
        super().atacar()

if __name__ == '__main__':
    le = Arqueiro('LEt')
    print(le.localizacao)