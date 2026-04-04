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
        self.inventory = Inventory() #Class
        #---attribute---
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        #---List_attribute---
        self.skill:list["Skill"] = [] #Create lsit name skill

    def take_damage(self , damage: int) -> int:
        actual = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual)
        return actual

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
        self.skill = [Slash()]

    def take_damage(self, damage: int) -> int:
        actual = super().take_damage(damage)
        self.rage = min(100 , self.rage + actual // 5)
        return actual


class Mage(Character):
    def __init__(self, name: str):
        super().__init__(name, hp=80, mp=120, attack=10, defense=5)
        self.spell_power = 30
        self.skill = [Fireball()]
    
    def special_ability(self , target: Character) -> str:
        cost = 40
        if self.mp < cost:
            return f"{self.name} not enough mp!"
        self.mp -= cost
        dmg = (self.spell_power * 3) - target.defense // 2
        actual = target.take_damage(dmg)
        return f"{self.name} use Meteor! deal {actual} magic damge!"

# ===================================
# ENEMY SYSTEM
# ===================================
class Enemy(Character):
    def __init__(self, name: str, hp: int, attack: int, defense: int, exp_reward: int):
        super().__init__(name, hp=hp, mp=0, attack=attack, defense=defense)
        self.exp_reward = exp_reward

    def special_ability(self, target: Character) -> str:
        dmg = int(self.attack * 1.5)
        actual = target.take_damage(dmg)
        return f"{self.name} use Berserk! deal {actual} damage"
    
    

# ===================================
# SKILL SYSTEM
# ===================================

class Skill(ABC):
    def __init__(self , name: str, mp_cost: int, description: str):
        self.name = name
        self.mp_cost = mp_cost
        self.description = description

    @abstractmethod
    def activate(self, user: Character, target: Character) -> str:
        pass
        
class Slash(Skill):
    def __init__(self):
        super().__init__("Slash", 5, "Make more damage")

    def activate(self, user, target):
        if user.mp < self.mp_cost:
            return "Mp isn't enough!"
        user.mp -= self.mp_cost
        actual = target.take_damage(user.attack + 10)
        return f"{user.name} use {self.name}! deal {actual} damage"

class Fireball(Skill):
    def __init__(self, name, mp_cost, description):
        super().__init__("Fireball", 20, "Fire magic , single damage")
    
    def activate(self, user: Mage, target):
        if user.mp < self.mp_cost:
            return "Mp isn't enough!"
        user.mp -= self.mp_cost
        dmg = user.spell_power * 2
        actual = target.take_damage(dmg)
        return f"{user.name} use {self.name}! deal {actual} magic damge"
# ===================================
# ITEM SYSTEM & INVENTORY SYSTEM
# ===================================

class Item(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def use(self, target: Character) -> str:
        pass

class HealthPotion(Item):
    def __init__(self, heal_amount: int = 50 ):
        super().__init__("Health Potion", f"heal Hp {heal_amount}")
        self.heal_amount = heal_amount

    def use(self, target: Character) -> str:
        actual = target.heal(self.heal_amount)
        return f"{target.name} use {self.name} heal {actual} Hp"
        
class ManaPotion(Item):
    def __init__(self, Mana_amount: 40):
        super().__init__("Mana Potion", f"Increase mana {Mana_amount}")
        self.Mana_amount = Mana_amount

    def use(self, target: Character):
        actual = min(self.Mana_amount, target.max_mp - target.mp)
        target.mp += actual
        return f"{target.name} use {self.name} increaes {actual} mp"


class Inventory:
    def __init__(self):
        self.item: list[Item] = [] #Only item in Item class can in this list

    def add(self, item: Item):
        self.item.append(item)
        print(f"add {item.name} to your inventory")

    def use(self, index: int, target: Character) -> str:
        if index >= len(self.item):
            return "You not have this item!"
        item = self.item.pop(index) #delete lsit want to delete (index of item)
        return item.use(target)
    
    def show(self):
        if not self.item:
            print("Your inventory is empty!")
        for i , item in enumerate(self.item):
            print(f"[{i}] {item.name} - {item.description}")

# ===================================
# BATTLE SYSTEM
# ===================================

class Battle:
    pass

 # ===================================
 # OUTPUT
 # ===================================

 