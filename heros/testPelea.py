from Game import *
from Hero import *

'''Se definen colores'''

r = [255,0,0]
g = [0,255,0]
b = [0,0,255]

o = [255,127,0]
y = [255,255,0]
i = [75,0,130]
v = [159,0,255]
e = [0,0,0]

imageHero1 = [
e,e,e,e,e,e,g,g,
e,e,e,e,e,g,g,g,
e,e,e,e,g,g,g,e,
r,r,e,g,g,g,e,e,
e,r,g,g,g,e,e,e,
e,e,r,g,e,e,e,e,
e,r,e,r,r,e,e,e,
r,e,e,e,r,e,e,e
]


hero1 = Hero("Pikcachu",100,imageHero1)
hero2 = Hero("Charizard",100,imageHero1)

g = Game()
g.fight(hero1,hero2)