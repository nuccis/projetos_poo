class Cenario:
    def __init__(self, name:str, inimigo:object, description:tuple) -> None:
        self.name = name
        self.inimigo = inimigo
        self.description = description
        self.descoberto = False
    
    def descrever(self):
        pass

    def checar_inimigos(self):
        pass

    def movimentar(self):
        pass