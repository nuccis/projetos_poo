from biblio.areas import mapa as mp
from biblio.inimigos import basicos as inb
from biblio.personagens import classes_jogador as jdr


let = jdr.Arqueiro('Nucis', mp.estrada_pedra)
print(let)

#Criar um menuzinho para andar pelos mapas e interagir com eles.
#Implementar a função descrever dos cenários
while True:
    print('Escolha uma opção: ')
    print('[1] Olhar ao redor\n'
          '[2] Procurar inimigos\n'
          '[3] Andar\n'
          '[4] Sair do jogo\n')
    opc = int(input('Opção desejada: '))
    if opc == 1:
        print(let)
    elif opc == 2:
        inimigo_vivo, inimigo = let.procurar_inimigos()
        if inimigo_vivo:
            while True:
                print('O que gostaria de fazer?\n'
                    '[1] Atacar\n'
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
    elif opc == 4:
        break

print('Até logo!')
