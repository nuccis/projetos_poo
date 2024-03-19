mapa = {
    'floresta':('cidade'),
    'cidade':('floresta', 'estrada escura', 'estrada de pedra', 'estrada de terra'),
    'estrada escura':('cidade'),
    'estrada de pedra':('cidade', 'campo'),
    'estrada de terra':('cidade','campo'),
    'campo':('estrada de terra', 'estrada de pedra')
}