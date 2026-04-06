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
        self.exp += amount
        if self.exp >= self.level *100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 3
        print(f"{self.name} level up! , reach to Level.{self.level}")

    def use_skill(self ,skill_index: int ,target: Character) -> str:
        if skill_index >= len(self.skill):
            return "There's no skill "
        skills = self.skill[skill_index]
        return skills.activate(self, target)
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
    
    def ai_action(self, target: Character) -> str:
        dmg = target.take_damage(self.attack + random.randint(-3, 5))
        return f"{self.name} attack {target.name} deal {dmg} damage"

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
    def __init__(self, Mana_amount: int=40):
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
    def __init__(self, player: Character, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 1

    def run(self):
        print(f"\n{'='*50}")
        print(f"Battle begin!")
        print(f"{self.player}")
        print(f"{self.enemy}")
        print(f"{'='*50}\n")

        while self.player.is_alive() and self.enemy.is_alive():
            print(f"--- turn {self.turn} ---")
            self._player_turn()
            if not self.enemy.is_alive():
                break
            self._enemy_turn()
            self.turn += 1
            print() #Empty space

        self._end_battle()
            

    def _player_turn(self):
        print(f"\n[player] Hp:{self.player.hp} MP:{self.player.mp}")
        print("1) attack 2)skill 3)special 4)item")
        choice = input("Choose: ").strip() #return choice to string

        if choice == "1":
            dmg = self.enemy.take_damage(self.player.attack)
            print(f"{self.player.name} attack! deal {dmg} damage")
        elif choice == "2":
            if self.player.skill:
                for i, skills in enumerate(self.player.skill):
                    print(f"[{i}] {skills.name} (MP:{skills.mp_cost}) - {skills.description}")
                skill_input = int(input("Choose skill: "))
                print(" " , self.player.use_skill(skill_input, self.enemy))
            else:
                print("No skill")

        elif choice == "3":
            print("Special ability if coming soon!")
        elif choice == "4":
            self.player.inventory.show()
            Inventory_Index_Input = input("Choose item(number): ")
            if Inventory_Index_Input.isdigit(): #Check if input is only number (return to bool)
                print(" ", self.player.inventory.use(int(Inventory_Index_Input) , self.player))
        
        else:
             print("skip turn")
    
        print(f"[Enemy] HP:{self.enemy.hp} / {self.enemy.max_hp}")

    def _enemy_turn(self):
        result = self.enemy.ai_action(self.player)
        print(f"{result}")
        print(f"[Player] Hp:{self.player.hp} / {self.player.max_hp}")

    def _end_battle(self):
        print(f"\n{'='*50}")
        if self.player.is_alive():
            print(f"{self.player.name} win!")
            self.player.gain_exp(self.enemy.exp_reward)
            print(f"You gain {self.enemy.exp_reward} EXP")
        else:
            print(f"{self.player.name} Loose!")
        print(f"{'='*50}\n")

 # ===================================
 # OUTPUT
 # ===================================

if __name__ == "__main__":
    #Create player character
    hero = Warrior("Arthur")
    hero.inventory.add(HealthPotion(60))
    hero.inventory.add(ManaPotion(30))

    #Create Enemy Character
    goblin_king = Enemy("Goblin King", hp=80, attack=18, defense=6, exp_reward=120)

    #Battle
    battle = Battle(hero, goblin_king)
    battle.run()

 