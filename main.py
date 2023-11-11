class Animal:
   def __init__(self, name):
       self.name = name
   def make_sound(self):
       pass
class Mammal(Animal):
   def __init__(self, name, fur_color):
       super().__init__(name)
       self.fur_color = fur_color
   def give_birth(self):
       pass
class Bird(Animal):
   def __init__(self, name, feather_color):
       super().__init__(name)
       self.feather_color = feather_color
   def lay_eggs(self):
       pass
class Platypus(Mammal, Bird):
   def __init__(self, name, fur_color, feather_color):
       Mammal.__init__(self, name, fur_color)
       Bird.__init__(self, name, feather_color)
   def make_sound(self):
       return "Muffled growl"
   def give_birth(self):
       return "Laying eggs"
   def lay_eggs(self):
       return "Laying eggs underwater"