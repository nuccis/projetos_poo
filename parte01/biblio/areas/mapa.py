mapa = {
    'inicio':('cidade'),
    'cidade':('inicio', 'estrada escura', 'estrada de pedra', 'estrada de terra'),
    'estrada escura':('cidade'),
    'estrada de pedra':('cidade', 'final'),
    'estrada de terra':('cidade','final'),
    'final':('estrada escura', 'estrada de pedra')
}