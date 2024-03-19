#Definição de classe
class Cenario:
    def __init__(self, nome:str, inimigo:object, description:tuple) -> None:
        self.nome = nome
        self.inimigo = inimigo
        self.description = description
        self.descoberto = False
    
    def descrever(self):
        pass

    def checar_inimigos(self):
        pass

    def movimentar(self, mapa):
        #Pensei em transformar o método movimentar em uma função geral, p conseguir utilizar outras funções em conjunto como por exemplo a leiaInteiro. Será uma função com retorno do objeto cenário escolhido.
        for v in mapa[self.nome]:
            print(f'{v.nome}'.capitalize())

#Teste
#Objetos
cidade = Cenario('cidade', 'nenhum', ('novo', 'antigo'))
floresta = Cenario('floresta', 'nenhum', ('novo', 'antigo'))
estrada_escura = Cenario('estrada escura', 'nenhum', ('novo', 'antigo'))
estrada_pedra = Cenario('estrada de pedra', 'nenhum', ('novo', 'antigo'))
estrada_terra = Cenario('estrada de terra', 'nenhum', ('novo', 'antigo'))
campo = Cenario('campo', 'nenhum', ('novo', 'antigo'))
#Mapa
'''mapa = {
    'floresta':('cidade'),
    'cidade':('floresta', 'estrada escura', 'estrada de pedra', 'estrada de terra'),
    'estrada escura':('cidade'),
    'estrada de pedra':('cidade', 'campo'),
    'estrada de terra':('cidade','campo'),
    'campo':('estrada de terra', 'estrada de pedra')
}'''
mapa = {
    'floresta':(cidade),
    'cidade':(floresta, estrada_escura, estrada_pedra, estrada_terra),
    'estrada escura':(cidade),
    'estrada de pedra':(cidade, campo),
    'estrada de terra':(cidade, campo),
    'campo':(estrada_terra, estrada_pedra)
}
#Programa
cidade.movimentar(mapa)