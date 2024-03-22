#Definição de classe
class Cidade:
    def __init__(self, nome:str, description:tuple) -> None:
        self.nome = nome
        self.description = description
        self.descoberto = False
    
    def descrever(self):
        pass

    def __repr__(self) -> str:
        return(f'{type(self).__name__}, '
                f'(nome = {self.nome}, '
                f'description = {self.description}, '
                f'descoberto = {self.descoberto})')