class Player:
    def __init__(self , name , hp , attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.inventory = []

class Enenmy:
    def __init__(self , name , hp , attack):
        self.name = name
        self.hp = hp
        self.attack = attack