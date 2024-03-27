from biblio.areas import mapa as mp
from biblio.inimigos import basicos as inb
from biblio.personagens import classes_jogador as jdr

#função


let = jdr.Arqueiro('Nucis', mp.floresta)

print(let)

#Criar a interação de combate entre o inimigo e o player
#Criar opções de saída do jogo: quando o jogador escolhe sair ou quando o jogador morre
#Configurar o cenário campo como o cenário final
#Criar um inventário para o player
#Configurar o cenário estrada escura com um loot para o player
while True:
    print('Escolha uma opção: ')
    print('[1] Olhar ao redor\n'
          '[2] Procurar inimigos\n'
          '[3] Andar\n'
          '[4] Sair do jogo\n')
    opc = int(input('Opção desejada: '))
    if opc == 1:
        let.localizacao.descrever()
    elif opc == 2:
        inimigo_vivo, inimigo = let.procurar_inimigos()
        if inimigo_vivo:
            while True:
                print('O que gostaria de fazer?\n'
                    '[1] Atacar\n'
                    '[2] Avaliar ameaça\n'
                    '[2] Ignorar\n')
                esc = int(input('Opção desejada: '))
                if esc == 2:
                    print(f'Você passa despercebido perante o {inimigo.nome}')
                    break
                elif esc == 1:
                    let.atacar(inimigo)
                    inimigo.status()
                    print(inimigo)
                    if not inimigo.vivo:
                        break
                    
                
    elif opc == 3:
        let.movimentar(mp.mapa)
        let.localizacao.descrever()
    elif opc == 4:
        break

print('Até logo!')


