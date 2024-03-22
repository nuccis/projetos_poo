from biblio.areas import mapa as mp
from biblio.inimigos import basicos as inb
from biblio.personagens import classes_jogador as jdr


let = jdr.Arqueiro('Nucis', mp.estrada_pedra)
print(let)
let.procurar_monstros()

#Criar um menuzinho para andar pelos mapas e interagir com eles.