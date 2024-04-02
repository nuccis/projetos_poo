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
              f'Localização: {self.localizacao.nome.capitalize()}'
              )
    
    def atacar(self, inimigo:object) -> None:
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
        self.localizacao.descoberto = True
        self.localizacao = mapa[self.localizacao.nome][resp - 1]

    
    def procurar_inimigos(self):
        #Aqui eu vou definir uma função que vai procurar inimigos e vai ter as seguintes condições:
        inimigo = ''
        #checar se self.localização é uma cidade
        if self.localizacao.tipo == 'cidade':
            print('Você se encontra na cidade e na cidade não há inimigos.')
        #Checar se self.localização.inimigo é uma instância
        elif type(self.localizacao.inimigo) is str:
            print('Não há inimigos por perto.')
        else:
            inimigo = self.localizacao.inimigo
        return inimigo
    
    def status(self):
        #aqui irá retornar textos para diferentes status do inimigo: vivo, ferido e morto
        if self.vida > 0 and self.vida < self.vidamax:
            print('Você possui alguns ferimentos pelo corpo')
        else:
            print('Você está caído sem vida no chão')
        print(f'A sua vida: {self.vida}/{self.vidamax}')
    

class Arqueiro(Personagem):
    def __init__(self, nome: str, localizacao: object) -> None:
        super().__init__(nome, 20, 3, localizacao)
    
    def atacar(self, inimigo: object) -> None:
        print('Você aponta o seu arco e atira')
        print(f'Infligindo {self.ataque} de dano ao {inimigo.nome}')
        return super().atacar(inimigo)
