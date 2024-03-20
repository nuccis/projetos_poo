#Definição de classe
class Cenario:
    def __init__(self, nome:str, inimigo:object, description:tuple) -> None:
        self.nome = nome
        self.inimigo = inimigo
        self.description = description
        self.descoberto = False
    
    def descrever(self):
        pass

    def __repr__(self) -> str:
        return(f'{type(self).__name__}, '
                f'(nome = {self.nome}, '
                f'inimigo = {self.inimigo}, '
                f'description = {self.description}, '
                f'descoberto = {self.descoberto})')
