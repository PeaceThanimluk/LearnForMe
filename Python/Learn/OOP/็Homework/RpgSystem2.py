class Character:


    def __init__(self , name , hp , attack):
        self.name = name
        self._hp = hp
        self._attack = attack

    def take_damage(self , damage):
        if isinstance(damage , int) and damage >= 0:
            if self._hp > 0 and self._hp - damage >= 0:
                self._hp -= damage
                print(f"{self.name} takes {damage} damage")
            else:
                self._hp = 0
        else:
            print("Invalid value!")

    def show_status(self):
        print(f"{self.name} Hp: {self._hp}")

    def is_alive(self):
        if self._hp > 0:
            return True
        else:
            return False
        
class Warrior(Character):

    def __init__(self , name , hp , atk):
        super().__init__(name , hp , atk)

    def slash(self , target):
        print(f"{self.name} uses slash!")

        damage = self._attack

        target.take_damage(damage)

        if not target.is_alive():
            print(f"{target.name} has been defeated!")

class Mage(Character):

    def __init__(self , name , hp , atk , mana):
        self._mana = mana
        super().__init__(name , hp , atk)

    def fireball(self , target):
        print(f"{self.name} uses fireball!")

        if self._mana > 10:
            self._mana -= 10

            damage = self._attack * 2

            target.take_damage(damage)

            if not target.is_alive():
                print(f"{target.name} has been defeated!")

        else:
            print("Not enough mana")

hero = Warrior("Knight", 100, 20)
enemy = Mage("Evil Mage", 80, 15, 50)

hero.slash(enemy)
enemy.fireball(hero)

hero.show_status()
enemy.show_status()