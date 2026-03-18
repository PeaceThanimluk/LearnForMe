from employee import Employee #ต้องอยู่ในfolderเดียวกันถึงจะimportได้
class Programmer(Employee):
    __DepartmentName = "โปรแกรมเมอร์"
    def __init__(self , name , salary , experience , skill):
        super().__init__(name , salary , self.__DepartmentName) #ใช้กับConstructor
        self.exp = experience
        self.skill = skill

    def ShowData(self): #Overriding method ชื่อ method เหมือนกันแต่ทำงานต่างกัน ขึ้นอยู่กับSubClass
        super().ShowData()
        print(f"Experience = {self.exp}")
        print(f"Skill = {self.skill}")

    def Calculate_Salary(self):
        pass