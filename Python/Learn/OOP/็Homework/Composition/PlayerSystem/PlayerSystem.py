class Health:
    def __init__(self , health):
        self.health = health

    def take_damage(self , damage):
        if isinstance(damage , int) and damage >= 0:
            self.health -= damage

            if self.health < 0:
                self.health = 0
        else:
            print("Invalid value")
    
    def is_alive(self):
        return self.health > 0

class Weapon:
    def __init__(self , name , damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return self.damage

class Player:
    def __init__(self , name):
        self.name = name
        self.weapon = Weapon("Sword" , 10)
        self.health = Health(100)

    def attack(self , enemy):
        if self.health.is_alive():
            damage = self.weapon.attack()
            enemy.health.take_damage(damage)
            print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name} is dead and can't attack!")


    def status(self):
        print(f"{self.name} Hp: {self.health.health}")
        if not self.health.is_alive():
            print(f"{self.name} is dead!")


p1 = Player("Hero")
p2 = Player("Monster")

p1.attack(p2)
p2.attack(p1)

p1.status()
p2.status()