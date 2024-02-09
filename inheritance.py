#inheritance
#Inheritance is a way of creating a new class for using details of an existing class without modifying it.

class Person:
    def move(self):
        print("Move 4 paces")
    def rest(self):
        print("Gain 4 health points")
        
class Doctor(Person):
    def heal(self):
        print("Heal 10 health points")
        
class Fighter(Person):
    def fight(self):
        print("Do 10 damage")  
    def move(self):
        print("Move 6 paces")
        
        
class Wizard(Doctor,Fighter):
    def cast_spell(self):
        print("Turns invisble")
    def heal(self):
        print("Heal 15 health points")
                
character1 = Doctor()
character1.move()

character1.heal()
character1=Fighter()
character1.fight()
character1.move()

character1=Wizard()
character1.cast_spell()