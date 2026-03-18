#PolyMorphism = การพ้องรูป เกิดจากpoly(หลากหลาย) + morphology(รูปแบบ)
#ข้อความเดียวกันแต่กระบวนการทำงานภายในแตกต่างกัน 
'''
ในทางโปรแกรมคือการที่Methodชื่อเดียวกัน สามารถรับarguement ที่แตกต่างกัน
ได้หลายรูปแบบ โดยmethodนี้จะถูกเรียกว่าoverload Method 
'''

#Overloading method = method ที่มีชื่อเหมือนกัน และอยุ่ภายในclass เดียวกัน
#สิ่งที่แยกความแตกต่างคือ parameter

"""
Overriding method = method ของ subclss ที่มีชื่อเหมือนกับ SuperCLass 
"""

#Overloading Method 
class Employee: #SuperClass
    #Variables
    MinSalary = 12000
    MaxSaraly = 50000
    _CompanyName = "SixSevenCompany"
    __Private = "Baka"


    def __init__(self , name , salary , Department): 
       #Instance Variable
        self.__name = name
        self.__salary = salary
        self._Department = Department

    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))

    #รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12
    
    def _getIncome(self , bonus = 0): #Overloading Method (Parameter ต่างกัน)
        return (self.__salary * 12) + bonus

    def __str__(self):
        return(f"ชื่อพนักงาน : {self.__name} , แผนก: {self._Department} , เงินเดือน: {self.__salary} , รายได้ต่อปี: {self._getIncome()}")

#SubClass
class Accounting(Employee): #Inheritance
    __DepartmentName = "บัญชี"
    def __init__(self , name , salary , age): #นำค่านำเข้าก่อน
        super().__init__(name , salary , self.__DepartmentName) #นำค่าที่ได้จากInitของAccountไปใส่ของEmployee
        self.age = age

    def ShowData(self): #Overriding method ชื่อ method เหมือนกันแต่ทำงานต่างกัน ขึ้นอยู่กับSubClass
        super().ShowData() #นำ method show data ของ SuperClass มาใช้ เพื่อแสดงผลข้อมูล name กับ salary ก่อน
        print(f"Age = {self.age}")

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

class Sale(Employee):
    __DepartmentName = "ขาย"
    def __init__(self , name , salary , area):
        super().__init__(name , salary , self.__DepartmentName)
        self.area = area

    def ShowData(self): #Overriding method ชื่อ method เหมือนกันแต่ทำงานต่างกัน ขึ้นอยู่กับSubClass
        super().ShowData()
        print(f"Area = {self.area}")


#crate object
Account = Accounting("FreeFire" , 20000 , 30)
programmer = Programmer("King" , 60000 , 2 , "Coding")
Sale = Sale("Baka" , 20000 , "Bangkok")


#Show data
# Account.ShowData()

print(f"MOney: {Account._getIncome(100)}")
