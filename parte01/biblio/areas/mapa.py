from . import cenarios as ce
from . import cidades as ci
from .. import inimigos as ig
from . import descricoes as desc

#Locais
cidade = ci.Cidade('cidade',(desc.cidade_desc_primeira_visita, desc.cidade_desc_segunda_visita))
floresta = ce.Cenario('floresta', 'nenhum', (desc.floresta_desc_primeira_visita, desc.floresta_desc_segunda_visita))
estrada_escura = ce.Cenario('estrada escura', 'nenhum', ('novo', 'antigo'))
estrada_pedra = ce.Cenario('estrada de pedra', ig.bestiario.lobo_sanguinario, (desc.estrada_de_pedra_desc_primeira_visita, desc.estrada_de_pedra_desc_segunda_visita))
estrada_terra = ce.Cenario('estrada de terra', ig.bestiario.urso_raivoso, (desc.estrada_de_terra_desc_primeira_visita, desc.estrada_de_terra_desc_segunda_visita))
campo = ce.Cenario('campo', 'nenhum', ('novo', 'antigo'))

#Mapa
mapa = {
    'floresta':(cidade,),
    'cidade':(floresta, estrada_escura, estrada_pedra, estrada_terra),
    'estrada escura':(cidade,),
    'estrada de pedra':(cidade, campo),
    'estrada de terra':(cidade, campo),
    'campo':(estrada_terra, estrada_pedra)
}

