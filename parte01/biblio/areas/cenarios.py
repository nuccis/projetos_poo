#Definição de classe
class Cenario:
    def __init__(self, nome:str, inimigo, description:tuple) -> None:
        self.nome = nome
        self.inimigo = inimigo
        self.description = description
        self.descoberto = False
        self.tipo = 'cenario'
    
    def descrever(self):
        if not self.descoberto:
            print(self.description[0])
        else:
            print(self.description[1])
        if type(self.inimigo) is not str:
            if self.inimigo.vida < self.inimigo.vidamax:
                print('Há marcas de sangue no chão devido à sua batalha recente') 
            if self.inimigo.vida == 0:
                self.inimigo.status()
 
            

    def __repr__(self) -> str:
        return(f'{type(self).__name__}, '
                f'(nome = {self.nome}, '
                f'inimigo = {self.inimigo}, '
                f'description = {self.description}, '
                f'descoberto = {self.descoberto.capitalize()})')
