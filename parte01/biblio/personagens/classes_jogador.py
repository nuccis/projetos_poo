from random import randint
from math import trunc
#Definição de classes
class Personagem:
    def __init__(self, nome:str, vida:int, ataque:int, localizacao:object) -> None:
        self.nome = nome
        self.vida = vida
        self.vidamax = vida
        self.ataque = ataque
        self.vivo = True
        self.localizacao = localizacao
        self._inventario = []
    
    #Funcionalidade da classe
    def __str__(self) -> str:
        return(f'Nome: {self.nome}\n'
              f'Vida: {self.vida}/{self.vidamax}\n'
              f'Ataque: {self.ataque}\n'
              f'Localização: {self.localizacao.nome.capitalize()}'
              )
    
    def atacar(self, inimigo:object) -> None:
        dano = randint(trunc(self.ataque*0.6), self.ataque)
        if inimigo.vida - dano <= 0:
            inimigo.vivo = False
            inimigo.vida = 0
        else:
            inimigo.vida -= dano
            print(f'Infligindo {dano} de dano ao {inimigo.nome}')

    def fugir (self, inimigo:object) -> None:
        fugir = randint(1,10)
        sucesso = False
        if fugir > 7:
            print(f'Você conseguiu fugir do {inimigo.nome}!')
            sucesso = True
        else:
            print(f'Você tenta fugir, porém o {inimigo.nome} consegue te alcançar!')
            inimigo.atacar(self)
            self.status()
        return sucesso
        
    def movimentar(self, mapa:dict):
        print('Caminhos disponíveis:')
        i=0
        for e in mapa[self.localizacao.nome]:
            i+=1
            print(f'[{i}] {e.nome.capitalize()}')
            
        resp = self.leInteiro('Digite a sua escolha: ', i)
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
            inimigo.status()
        return inimigo
    
    def status(self):
        #aqui irá retornar textos para diferentes status do inimigo: vivo, ferido e morto
        if self.vida > 0 and self.vida < self.vidamax:
            print('Você possui alguns ferimentos pelo corpo')
        else:
            print('Você está caído sem vida no chão')
        print(f'A sua vida: {self.vida}/{self.vidamax}')

    def mostar_inventario(self):
        if len(self.inventario) == 0:
            print('Seu inventário está vázio')
        else:
            print(f'{'\033[32m===INVENTARIO===\033[m':^30}')
            i=0
            for item in self.inventario:
                i+=1
                print(f'[{i}] {item.nome}') 
            print(f'[{len(self.inventario)+1}] Fechar inventário')
            opc = self.leInteiro('Opção desejada: ', i+1)
            if opc - 1 < len(self.inventario):
                self.inventario[opc-1].usar(self)
                print(f'O objeto "{self.inventario[opc-1].nome}" foi utilizado')
                self.inventario.pop(opc-1)            

    def vasculhar_objetos(self):
        if self.localizacao.tipo == 'cidade' or type(self.localizacao.item) is str:
            print('Não há nenhum objeto por perto')
        else:
            print(f'Você encontra um objeto do tipo: {self.localizacao.item.nome}')
            print(f'E o objeto se encontrava: {self.localizacao.item.descricao}')
            print('O que gostaria de fazer?\n'
                    '\033[96m[1]\033[m Pegar\n'
                    '\033[96m[2]\033[m Deixar onde está'
                    )
            opc = self.leInteiro('Opção desejada: ', 2)
            if opc == 1:
                print(f'O objeto "{self.localizacao.item.nome}" foi adicionado ao seu invetário!')
                self.inventario = self.localizacao.item
                self.localizacao.item = 'nenhum'      

    #Setter e Getter
    @property
    def inventario(self):
        return self._inventario

    @inventario.setter
    def inventario(self, value):
        if len(self._inventario) < 2:
            self._inventario.append(value)
        else:
            print('O inventário está cheio')
    
    #Métodos Estáticos
    @staticmethod
    def leInteiro(msg:str, rng:int) -> int:
        while True:
            try:
                opc = int(input(msg))
                if opc not in range(1, rng+1):
                    raise ValueError
                break
            except ValueError:
                print('\033[0;31mErro! Digite uma opção válida.\033[m')
        return opc
    

class Arqueiro(Personagem):
    def __init__(self, nome: str, localizacao: object) -> None:
        super().__init__(nome, 20, 3, localizacao)
    
    def atacar(self, inimigo: object) -> None:
        print('Você aponta o seu arco e atira')
        return super().atacar(inimigo)
