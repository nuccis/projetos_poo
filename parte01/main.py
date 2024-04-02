from biblio.areas import mapa as mp
from biblio.inimigos import basicos as inb
from biblio.personagens import classes_jogador as jdr

#função
def cor(cor, text):
    return f'\033[{cor}m{text}\033[m'

let = jdr.Arqueiro('Nucis', mp.estrada_pedra)

print(let)

#Criar a interação de combate entre o inimigo e o player: feito
#Criar opções de saída do jogo: quando o jogador escolhe sair ou quando o jogador morre: feito
#Configurar o cenário campo como o cenário final
#Criar um inventário para o player -> será uma lista com 2 espaços
#Configurar o cenário estrada escura com um loot para o player
#Criar uma condição de vitória para o jogo
while True:
    print('Escolha uma opção: ')
    print(f'{cor(96,'[1]')} Olhar ao redor\n'
          f'{cor(96,'[2]')} Procurar inimigos\n'
          f'{cor(96,'[3]')} Andar\n'
          f'{cor(96,'[4]')} Sair do jogo\n')
    opc = int(input('Opção desejada: '))
    if opc == 1:
        let.localizacao.descrever()
    elif opc == 2:
        inimigo = let.procurar_inimigos()
        inimigo.status()
        if inimigo.vivo:
            while True:
                print('O que gostaria de fazer?\n'
                    f'{cor(96,'[1]')} Atacar\n'
                    f'{cor(96,'[2]')} Avaliar ameaça\n'
                    f'{cor(96,'[3]')} Ignorar\n')
                esc = int(input('Opção desejada: '))
                if esc == 3:
                    print(f'Você passa despercebido perante o {inimigo.nome}')
                    break
                elif esc == 1:
                    let.atacar(inimigo)
                    inimigo.status()
                    if not inimigo.vivo:
                        break
                    inimigo.atacar(let)
                    let.status()
                    if not let.vivo:
                        break
                elif esc == 2:
                    print(cor(36, '\nStatus do Inimigo'))
                    print(inimigo)                        
    elif opc == 3:
        let.movimentar(mp.mapa)
        let.localizacao.descrever()
    elif opc == 4:
        break
    if not let.vivo:
        print('Você morreu.')
        break

print('Até logo!')


