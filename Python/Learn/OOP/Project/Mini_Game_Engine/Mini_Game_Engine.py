from abc import ABC , abstractmethod

# ===================================
# CHATACTER CLASS
# ===================================

class Character(ABC):

    def __init__(self , name: str , hp: int , mp : int , attack : int , defense : int):
        #defalut_attribute
        self.name = name
        self.max_hp = hp
        self.max_mp = mp
        self.level = 1
        self.exp = 0
        self.Inventory = Inventory() #Class
        #attribute
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        #List_attribute
        self.skill:list["Skill"] = [] #Create lsit name skill

# ===================================
# PLAYER CLASS
# ===================================
'''
Create class by use inheritance
-Warrior 
-Mage
'''

class Warrior(Character):
    pass

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

 