#Constructor ใช้งานเมื่อเริ่มต้นสร้างวัตถุ
'''โครงสร้างConstructor
def__init__(self):
    pass
'''

class Employee:

    def __init__(self , name , salary): 
        self.name = name
        self.salary = salary
    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.name))
        print("Salary = {}".format(self.salary))
    

obj1 = Employee("peace" , 10)
obj2 = Employee("monk" , 100)
obj1.ShowData()
obj2.ShowData()