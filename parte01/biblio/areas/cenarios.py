class Cenario:
    def __init__(self, name:str, inimigos:list, description:dict) -> None:
        self.name = name
        self.inimigos = inimigos
        self.description = description
        self.descoberto = False
    
    def menu(self):
        pass

    def descrever(self):
        pass

    def checar_inimigos(self):
        pass

    def movimentar(self):
        pass