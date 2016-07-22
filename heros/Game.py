from Hero import *

class Game:


  def win(self,hero1,hero2):
      if hero1.level > hero2.level:
          print "Gana hero: ", hero1.name, hero1.level
      else:
          print "Gana hero: ", hero2.name, hero2.level