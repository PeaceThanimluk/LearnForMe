class BankAccount:

    def __init__(self , name , amount): #Create data
        self.__name = name
        self.__amount = amount

    def deposit(self , amount):
        if isinstance(amount , int):
            self.__amount += amount


    def withdraw(self , amount):
        if amount <= self.__amount:
            self.__amount -= amount

    def get_balance(self):
        return self.__amount


acc = BankAccount("John" , 1000)

acc.deposit(500)
acc.withdraw(200)

print(acc.get_balance())