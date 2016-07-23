from Hero import *
from Printer import *
import random as r
import time as t

class Game:

  printer = Printer()

  def win(self,hero1,hero2):
      if hero1.level > hero2.level:
          print "Gana : ", hero1.name, hero1.level
          self.printer.printIcon(hero1)
      else:
          print "Gana : ", hero2.name, hero2.level
          self.printer.printIcon(hero2)


  def fight(self,hero1,hero2,sense):
      count   = 0
      while count < True :
          if r.random() >= 0.5:
              hero1.level = hero1.level - 1
              self.printer.printIcon(hero2,sense)
              print "Golpe ", hero2.name, hero2.level
          else:
              hero2.level = hero2.level - 1
              self.printer.printIcon(hero1,sense)
              print "Golpe ", hero1.name, hero1.level
          if hero1.level <=0 or hero2.level <= 0:
              self.win(hero1,hero2)
              return 0
          t.sleep(.5)
