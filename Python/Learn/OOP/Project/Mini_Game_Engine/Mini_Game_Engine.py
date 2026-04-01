from abc import ABC , abstractmethod
import random

# ===================================
# CHATACTER CLASS
# ===================================

class Character(ABC):

    def __init__(self , name: str , hp: int , mp : int , attack : int , defense : int):
        #---defalut_attribute---
        self.name = name
        self.max_hp = hp
        self.max_mp = mp
        self.level = 1
        self.exp = 0
        #---attribute---
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        #---List_attribute---
        self.skill:list["Skill"] = [] #Create lsit name skill

    #---Abstract Method---
    @abstractmethod
    def basic_attack(self , target):
        pass

    @abstractmethod
    def take_damage(self , damage):
        pass

    #---Function---
    def is_alive(self) -> bool:
        return self.hp > 0

    def heal(self , amount: int):
        actual = min(amount , self.max_hp - self.hp) 
        #เลือกค่าที่น้อยที่สุดระหว่าง amount กับเลือดที่หายไป
        #เพื่อป้องกันไม่ให้healเกินหลอดของhp
        #ถ้าamountมีค่ามากกว่า self.max_hp - self.hp(ค่าที่เลือดหายไป) จะใช้ค่านั้นแทน จะกลายเป็นเลือดกลับมาเต็ม
        self.hp += actual
        return actual

    def gain_exp(self , amount : int):
        pass

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 3
        print(f"{self.name} level up! , reach to Level.{self.level}")

    

# ===================================
# PLAYER CLASS
# ===================================
'''
Create class by use inheritance
-Warrior 
-Mage
'''

class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name, hp=150, mp=30, attack=25, defense=15)
        self.rage = 0
        self.skill = [Slash]

class Mage(Character):
    pass

# ===================================
# ENEMY SYSTEM
# ===================================
class Enemy(Character):
    pass

# ===================================
# SKILL SYSTEM
# ===================================

class Skill(ABC):
    pass

class Slash(Skill):
    pass

class Fireball(Skill):
    pass

# ===================================
# ITEM SYSTEM & INVENTORY SYSTEM
# ===================================

class Item(ABC):
    pass

class Potions(Item):
    pass

class Weapons(Item):
    pass


class Inventory:
    pass

# ===================================
# BATTLE SYSTEM
# ===================================

class Battle:
    pass

 # ===================================
 # OUTPUT
 # ===================================

 