class Player:

    def __init__(self , name , hp):
        self.name = name
        self._hp = hp
        self.__exp = 0
        self.__level = 1

    def take_damage(self , damage):
        if isinstance(damage , int) and damage >= 0:
            if self._hp - damage >= 0:
                self._hp -= damage
            else:
                self._hp = 0
            print(f"{self.name} took {damage} damage")
        else:
            print("Invalid value!")

    def heal(self , amount):
        if isinstance(amount , int) and amount >= 0:
            if self._hp + amount <= 100:
                self._hp += amount
            else:
                self._hp = 100
            print(f"{self.name} healed {amount} Hp")
        else:
            print("Invalid value!")

    def gain_exp(self , exp):
        if isinstance(exp , int) and exp >= 0:
            if self.__exp + exp >= 100:
                self.__level += (self.__exp + exp) // 100
                self.__exp = (self.__exp + exp) % 100
                print("level up!")
            else:
                self.__exp += exp
        else:
            print("Invalid value!")
        
    def show_status(self):
         print(f"Name: {self.name}")
         print(f"Hp: {self._hp}")
         print(f"Level: {self.__level}")
         print(f"Exp: {self.__exp}")


p1 = Player("Hero", 100)

p1.take_damage(30)
p1.heal(10)

p1.gain_exp(50)
p1.gain_exp(60)

p1.show_status()