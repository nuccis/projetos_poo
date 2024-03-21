from biblio.areas import mapa as mp
from biblio.inimigos import basicos as inb
from biblio.personagens import classes_jogador as jdr


let = jdr.Arqueiro('Nucis', mp.floresta)
print(let)
let.movimentar(mp.mapa)
print(let)
let.movimentar(mp.mapa)
print(let)
#Criar um menuzinho para andar pelos mapas e interagir com eles.