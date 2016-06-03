import pygame

from pygame.locals import *
from sense_hat import SenseHat
from Point import *

pygame.init()
pygame.display.set_mode((640, 480))

sense = SenseHat()
sense.clear()

point1 = Point(0,0)
point2 = Point(0,1)
point3 = Point(0,2)

gusano = [point1,point2,point3]

running = True

x = 0
y = 2
#sense.set_pixel(x, y, 255, 255, 255)
white = (255,255,255)

paintGusano(gusano,sense,white)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #sense.set_pixel(x, y, 0, 0, 0)  # Black 0,0,0 means OFF

            if event.key == K_DOWN and y < 7:
                y = y + 1
            elif event.key == K_UP and y > 0:
                y = y - 1
            elif event.key == K_RIGHT and x < 7:
                x = x + 1
            elif event.key == K_LEFT and x > 0:
                x = x - 1
        sense.clear()
        pointTemp = Point(x,y) 
        updateGusano(gusano,pointTemp)
        paintGusano(gusano,sense,color)
        #sense.set_pixel(x, y, 255, 255, 255)
        if event.type == QUIT:
            running = False
            print("BYE")
 
 def borrarPantalla(sense):
    sense.clear()

 def paintGusano(gusano,sense,color):

    for point in len(gusano):
        sense.set_pixel(point.x,point.y,color)


 def updateGusano(gusano,bloque):
    count  = len(gusano)-1
    lstNuevoGusano = range(len(gusano))
    #Recorre el gusano antiguo y lo pone en el nuevo pero descartando
    #la ultima posicion
    while count > 0 :
        lstNuevoGusano[count] = gusano[count-1]
        count = count - 1
    lstNuevoGusano[0] = bloque

    return lstNuevoGusano

def addGusano(gusano,bloque):
    count  = len(gusano)-1
    lstNuevoGusanoNew = range(len(gusano)+1)
    #Recorre el gusano antiguo y lo pone en el nuevo pero descartando
    #la ultima posicion
    while count > 0 :
        lstNuevoGusanoNew[count] = gusano[count-1]
        count = count - 1
    lstNuevoGusanoNew[0] = bloque

    return lstNuevoGusanoNew
