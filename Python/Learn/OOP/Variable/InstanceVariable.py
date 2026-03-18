#Instance variable = ตัวแปรที่อยู่ภายใน object สามารถเข้าถึงข้อมูลส่วนนี้โดยการสร้าง object ขึ้นมา

class Employee:

    def __init__(self , name , salary): 
       #Instance Variable
        self.__name = name
        self.__salary = salary

    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))
    
#Create Object
obj1 = Employee("peace" , 10)