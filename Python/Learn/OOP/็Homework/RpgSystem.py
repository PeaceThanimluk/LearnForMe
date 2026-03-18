#SuperClass
class character:

    def __init__(self , name , hp , attack_power):
        self.name = name
        self._hp = hp
        self._atk = attack_power

    def show_status(self):
        print(f"Name : {self.name}")
        print(f"Hp : {self._hp}")
        print(f"Attack : {self._atk}")

#SubClass
class Warrior(character): #Create SubClass of character class(SuperClass)
    def __init__(self, name, hp, attack_power , defense): #Create new Attribute(Defense)
        super().__init__(name, hp, attack_power)#Use Method of character class
        self.defense = defense #Create new self attribute

    def block(self): #Create new method of warrior class
        print(f"{self.name} blocks the attack!")

class Mage(character):
    def __init__(self, name, hp, attack_power , mana):
        super().__init__(name, hp, attack_power)      
        self.mana = mana  

    def cast_spell(self):
        print(f"{self.name} casts a fireball!")

class Archer(character):
    def __init__(self, name, hp, attack_power , arrows):
        super().__init__(name, hp, attack_power)
        self.arrows = arrows

    def shoot_arrow(self):
        print(f"{self.name} shoots an arrows!")

#Create objects
warrior = Warrior("Thor", 120, 25, 10)
mage = Mage("Merlin", 80, 30, 100)
archer = Archer("Legolas", 90, 20, 30)

#Use method / Output
warrior.show_status()
warrior.block()

mage.cast_spell()

archer.shoot_arrow()