from biblio.areas import mapa as mp
#from biblio.inimigos import basicos as inb
from biblio.personagens import classes_jogador as jdr

#função
def cor(cor, text):
    return f'\033[{cor}m{text}\033[m'

jogador = jdr.Arqueiro('Nucis', mp.estrada_escura)


print(jogador)

#Criar a interação de combate entre o inimigo e o player: feito
#Criar opções de saída do jogo: quando o jogador escolhe sair ou quando o jogador morre: feito
#Configurar o cenário campo como o cenário final: adicionar o dragão nos inimigos do cenário e criar ele com o tipo 'final'. e na batalha configurar para caso o monstro morra e o personagem esteja em um cenário do tipo final, ele ganhe o jogo
#Criar um inventário para o player -> será uma lista com 2 espaços: feito
#Configurar o cenário estrada escura com um loot para o player: feito
#configurar o menu com vasculhar objeto: feito
#configurar o menu com inventário: feito
#Configurar para utilizar os itens do inventário: feito
#configurar o menu com mostrar os seus status: feito
#Criar uma condição de vitória para o jogo

while True:
    print(f'\n{cor(96,'====MENU===='):^30}')
    print(f'{cor(96,'[1]')} Olhar ao redor\n'
          f'{cor(96,'[2]')} Procurar inimigos\n'
          f'{cor(96,'[3]')} Vasculhar por objetos\n'
          f'{cor(96,'[4]')} Inventário\n'
          f'{cor(96,'[5]')} Mostrar seus status\n'
          f'{cor(96,'[6]')} Andar\n'
          f'{cor(96,'[7]')} Sair do jogo\n')
    opc = int(input('Opção desejada: '))
    if opc == 1:
        jogador.localizacao.descrever()
    elif opc == 2:
        inimigo = jogador.procurar_inimigos()      
        if type(inimigo) is not str and inimigo.vivo:
            inimigo.status()
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
                    jogador.atacar(inimigo)
                    inimigo.status()
                    if not inimigo.vivo:
                        break
                    inimigo.atacar(jogador)
                    jogador.status()
                    if not jogador.vivo:
                        break
                elif esc == 2:
                    print(cor(36, '\nStatus do Inimigo'))
                    print(inimigo)                        
    elif opc == 3:
        jogador.vasculhar_objetos()
    elif opc == 4:
        jogador.mostar_inventario()
    elif opc == 5:
        print(f'\n{cor(94,'====STATUS DO JOGADOR===='):^35}')
        print(jogador)
    elif opc == 6:
        jogador.movimentar(mp.mapa)
        jogador.localizacao.descrever()
    elif opc == 7:
        break
    if not jogador.vivo:
        print('Você morreu.')
        break

print('Até logo!')


