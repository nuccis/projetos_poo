#Definição de classe
class Cenario:
    def __init__(self, nome:str, inimigo, description:tuple, item, tipo = 'cenario') -> None:
        self.nome = nome
        self.inimigo = inimigo
        self.description = description
        self.descoberto = False
        self.item = item
        self.tipo = tipo
    
    def descrever(self):
        if not self.descoberto:
            linhas = self.description[0].split('\n')
            for linha in linhas:
                print(f'\033[0;34m{linha.center(100)}\033[m')
        else:
            linhas = self.description[1].split('\n')
            for linha in linhas:
                print(f'\033[0;34m{linha.center(100)}\033[m')
        if type(self.inimigo) is not str:
            if self.inimigo.vida < self.inimigo.vidamax:
                print('Há marcas de sangue no chão devido à sua batalha recente'.center(100)) 
            if self.inimigo.vida == 0:
                self.inimigo.status().center(100)          

    def __repr__(self) -> str:
        return(f'{type(self).__name__}, '
                f'(nome = {self.nome}, '
                f'inimigo = {self.inimigo}, '
                f'description = {self.description}, '
                f'descoberto = {self.descoberto.capitalize()})')
