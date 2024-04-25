from biblio.areas import mapa as mp
#from biblio.inimigos import basicos as inb
from biblio.personagens import classes_jogador as jdr

#função
def cor(cor, text):
    return f'\033[{cor}m{text}\033[m'

def batalha(jogador, inimigo, fim_jogo):

    while True:
        print('O que gostaria de fazer?\n'
            f'{cor(96,'[1]')} Atacar\n'
            f'{cor(96,'[2]')} Avaliar ameaça\n'
            f'{cor(96,'[3]')} Fugir\n')
        esc = int(input('Opção desejada: '))
        if esc == 3:
            if jogador.fugir(inimigo):
                break
        elif esc == 1:
            jogador.atacar(inimigo)
            inimigo.status()
            if not inimigo.vivo:
                if jogador.localizacao.tipo == 'final':
                    fim_jogo = True
                break
            inimigo.atacar(jogador)
            jogador.status()
            if not jogador.vivo:
                break
        elif esc == 2:
            print(cor(36, '\nStatus do Inimigo'))
            print(inimigo)   
    return fim_jogo                     

#Variáveis
fim_jogo = False
desfecho_vitoria = ('Com um golpe final certeiro, você derrota o draco negro,\n'
                    'cujo corpo imponente desaba no chão do campo.\n'
                    'Um silêncio solene preenche o ar,\n'
                    'enquanto você observa o horizonte em busca de qualquer sinal de perigo.\n'
                    'A paz finalmente retorna à terra,\n'
                    'e você sabe que sua coragem e determinação prevaleceram.\n'
                    'Você é saudado como herói pelo povo do vilarejo,\n'
                    'e seu nome será lembrado nas canções e histórias por gerações vindouras.\n'
                    '\n'
                    'Você venceu!\n'
                    'Seu destino está agora nas suas mãos,\n'
                    'e novas aventuras aguardam além do horizonte.'
                    )
jogador = jdr.Arqueiro('Nucis', mp.campo)


print(jogador)

#Criar a interação de combate entre o inimigo e o player: feito
#Criar opções de saída do jogo: quando o jogador escolhe sair ou quando o jogador morre: feito
#Configurar o cenário campo como o cenário final: adicionar o dragão nos inimigos do cenário e criar ele com o tipo 'final'. e na batalha configurar para caso o monstro morra e o personagem esteja em um cenário do tipo final, ele ganhe o jogo: feito
#Criar um inventário para o player -> será uma lista com 2 espaços: feito
#Configurar o cenário estrada escura com um loot para o player: feito
#configurar o menu com vasculhar objeto: feito
#configurar o menu com inventário: feito
#Configurar para utilizar os itens do inventário: feito
#configurar o menu com mostrar os seus status: feito
#Criar uma condição de vitória para o jogo: feito
#Criar uma lógica para chance de conseguir fugir do inimigo: feito
#Criar um range para o ataque (2 - 4): feito
#Testar o jogo em partidas diferentes: feito
#Criar as validações de entrada:
#Criar o menu de criação do personagem:
#Melhorar a formatação e a apresentação visual:
#Fazer a documentação:

while True:
    print(f'\n{cor(96,'====MENU===='):^30}')
    print(f'{cor(96,'[1]')} Olhar ao redor\n'
          f'{cor(96,'[2]')} Procurar por inimigos\n'
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
            fim_jogo = batalha(jogador, inimigo, fim_jogo)                   
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
        if jogador.localizacao.tipo != 'cidade':
            inimigo = jogador.localizacao.inimigo
            if type(inimigo) is not str and inimigo.vivo:
                print('\n',cor(91,f'Enquanto você adentra o/a {jogador.localizacao.nome}'.center(100)))
                print(cor(91,f'um {inimigo.nome} surge das sombras, pronto para te desafiar.'.center(100)))
                fim_jogo = batalha(jogador, inimigo, fim_jogo)    
    elif opc == 7:
        break
    if not jogador.vivo:
        print('Você morreu.')
        break
    if fim_jogo:
        linhas = desfecho_vitoria.split('\n')
        for linha in linhas:
            print(f'\033[0;34m{linha.center(100)}\033[m')
        break
print('Até logo!')
