#Definição de classe
class Cidade:
    def __init__(self, nome:str, description:tuple) -> None:
        self.nome = nome
        self.description = description
        self.descoberto = False
        self.tipo = 'cidade'
    
    def descrever(self):
        if not self.descoberto:
            linhas = self.description[0].split('\n')
            for linha in linhas:
                print(f'\033[0;34m{linha.center(100)}\033[m')
        else:
            linhas = self.description[1].split('\n')
            for linha in linhas:
                print(f'\033[0;34m{linha.center(100)}\033[m')

    def __repr__(self) -> str:
        return(f'{type(self).__name__}, '
                f'(nome = {self.nome}, '
                f'description = {self.description}, '
                f'descoberto = {self.descoberto})')