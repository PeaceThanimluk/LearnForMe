class Character:


    def __init__(self , name , hp , attack): #Create Attribute
        self.name = name
        self._hp = hp
        self._attack = attack

    def take_damage(self , damage): #Create take_damage method 
        if isinstance(damage , int) and damage >= 0: #Check if damage is int and damge >=0
            if self._hp > 0 and self._hp - damage >= 0: #Check if hp > 0 and  result is not dead
                self._hp -= damage #Take damage (decrease hp from damage)
                print(f"{self.name} takes {damage} damage")
            else:
                self._hp = 0 #(if result hp < 0 then set it to hp 0 )
        else:
            print("Invalid value!")

    def show_status(self):
        print(f"{self.name} Hp: {self._hp}")

    def is_alive(self): #Check if hp > 0 by return true or false
        if self._hp > 0:
            return True
        else:
            return False
        
class Warrior(Character): #Create SubClass Name Warrior

    def __init__(self , name , hp , atk): #Create inheritance 
        super().__init__(name , hp , atk) #Use super() to use init of SuperClass(Character)

    def slash(self , target): #Create slash method
        print(f"{self.name} uses slash!")

        damage = self._attack #set attribute 
        #target = object(class)
        target.take_damage(damage) #object use take_damage method 

        if not target.is_alive():
            print(f"{target.name} has been defeated!")

class Mage(Character):

    def __init__(self , name , hp , atk , mana):
        self._mana = mana
        super().__init__(name , hp , atk)

    def fireball(self , target):
        print(f"{self.name} uses fireball!")

        if self._mana >= 10: #Create mana system: mana require to use skill is 10
            self._mana -= 10

            damage = self._attack * 2 #if class mage then damage will multiple 2

            target.take_damage(damage)

            if not target.is_alive():
                print(f"{target.name} has been defeated!")

        else:
            print("Not enough mana")

#Create objects
hero = Warrior("Knight", 100, 20)
enemy = Mage("Evil Mage", 80, 15, 50)

#Object use method
hero.slash(enemy)
enemy.fireball(hero)

#Show status
hero.show_status()
enemy.show_status()