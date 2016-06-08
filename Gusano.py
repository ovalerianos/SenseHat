import pygame

from pygame.locals import *
from sense_hat import SenseHat
from Point import *
import time
from random import randint

class Gusano:

 sense = 0
 gusano= -1 
 running = True
 white = (0,0,0)
 red   = (255,0,0)
 comida= Point(-1,-1)

 def __init__(self):
  self.sense = SenseHat()
  self.sense.clear()
  self.white = (255,255,255)
  point1 = Point(0,0)
  point2 = Point(0,1)
  point3 = Point(0,2)
  self.gusano = [point3,point2,point1]

 def run(self):
  #sense.set_pixel(x, y, 255, 255, 255)
  pygame.init()
  pygame.display.set_mode((640, 480))
  x = 0
  y = 2
  print self.gusano
  self.paintGusano()
  while self.running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            #sense.set_pixel(x, y, 0, 0, 0)  # Black 0,0,0 means OFF
            update = False
            if event.key == K_DOWN and y < 7:
                y = y + 1
                update=True
            elif event.key == K_UP and y > 0:
                y = y - 1
                update=True
            elif event.key == K_RIGHT and x < 7:
                x = x + 1
                update=True
            elif event.key == K_LEFT and x > 0:
                x = x - 1
                update=True
            pointTemp = Point(x,y)
            print '-----   Posicion'
            print pointTemp.x
            print pointTemp.y
            print '-----EndPosicion'
            if update == True and self.ifExistPoint(self.gusano,pointTemp) == False: 
              print 'Evento------' 
              self.sense.clear()
              self.gusano = self.updateGusano(self.gusano,pointTemp)
              self.paintGusano()
              print '____________________________________________'
              self.comiendo(pointTemp)

            if self.comidaDisponible() == False:
                self.comida = self.generaComida()
        #sense.set_pixel(x, y, 255, 255, 255)
        if event.type == QUIT:
            self.running = False
            print("BYE")
        time.sleep(0.15)


 def paintGusano(self):
    print 'Imprimiendo gusano'
    #max = len(self.gusano)-1
    for i in range(len(self.gusano)):
        color=self.white
        point = self.gusano[i]
        print '**************'
        print point.x
        print point.y
        print '**************'
        if i == 0:
            color=self.red
        else:
            color=self.white
        self.sense.set_pixel(point.x,point.y,color)

 def ifExistPoint(self,gusano,pointX):
    for i in range(len(gusano)):
        point = gusano[i]
        if point.x == pointX.x and point.y == pointX.y:
            return True

    return False

 def updateGusano(self,gusano,bloque):
    print 'Update Gusano'
    print bloque.x
    print bloque.y
    count  = len(gusano)-1
    lstNuevoGusano = range(len(gusano))
    #Recorre el gusano antiguo y lo pone en el nuevo pero descartando
    #la ultima posicion
    while count > 0 :
        lstNuevoGusano[count] = gusano[count-1]
        count = count - 1
    lstNuevoGusano[0] = bloque

    return lstNuevoGusano

 def addGusano(self,gusano,bloque):
    print 'Gusano Comiendo'
    count  = len(gusano)-1
    lstNuevoGusanoNew = range(len(gusano)+1)
    #Recorre el gusano antiguo y lo pone en el nuevo pero descartando
    #la ultima posicion
    while count > 0 :
        lstNuevoGusanoNew[count] = gusano[count-1]
        count = count - 1
    lstNuevoGusanoNew[0] = bloque

    return lstNuevoGusanoNew

 def comiendo(self,bloque):
     if bloque.x == self.comida.x and bloque.y == self.comida.y:
        self.gusano = self.addGusano(self.gusano,bloque)


 
 def comidaDisponible(self):
     if self.comida.x != -1 and self.comida.y !=-1:
        return True
     else:
        return False


 def generaComida(self):
    bandera  = True
    comindaX = Point(-1,-1)
    while bandera:
     comindaX = Point(randint(0,7),randint(0,7))
     bandera =  self.ifExistPoint(self.gusano,comindaX)

    return comindaX
    




