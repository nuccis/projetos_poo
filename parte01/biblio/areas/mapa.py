import cenarios as ce
import cidades as ci

#Locais
cidade = ci.Cidade('cidade', 'nenhum', ('novo', 'antigo'))
floresta = ce.Cenario('floresta', 'nenhum', ('novo', 'antigo'))
estrada_escura = ce.Cenario('estrada escura', 'nenhum', ('novo', 'antigo'))
estrada_pedra = ce.Cenario('estrada de pedra', 'nenhum', ('novo', 'antigo'))
estrada_terra = ce.Cenario('estrada de terra', 'nenhum', ('novo', 'antigo'))
campo = ce.Cenario('campo', 'nenhum', ('novo', 'antigo'))

#Mapa
mapa = {
    'floresta':(cidade),
    'cidade':(floresta, estrada_escura, estrada_pedra, estrada_terra),
    'estrada escura':(cidade),
    'estrada de pedra':(cidade, campo),
    'estrada de terra':(cidade, campo),
    'campo':(estrada_terra, estrada_pedra)
}

