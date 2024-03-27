#Definição de classe
class Cidade:
    def __init__(self, nome:str, description:tuple) -> None:
        self.nome = nome
        self.description = description
        self.descoberto = False
        self.tipo = 'cidade'
    
    def descrever(self):
        if not self.descoberto:
            print(self.description[0])
        else:
            print(self.description[1])

    def __repr__(self) -> str:
        return(f'{type(self).__name__}, '
                f'(nome = {self.nome}, '
                f'description = {self.description}, '
                f'descoberto = {self.descoberto})')