#super() ใช้เมื่อต้องการที่จะเรียกใช้งานคุณสมบัติต่างๆในSuperclass
#เช่น Constructor , Method , attriubute

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

#SubClass
class Accounting(Employee): #Inheritance
    __DepartmentName = "บัญชี"
    def __init__(self , name , salary): #นำค่านำเข้าก่อน
        super().__init__(name , salary , self.__DepartmentName) #นำค่าที่ได้จากInitของAccountไปใส่ของEmployee

class Programmer(Employee):
    __DepartmentName = "โปรแกรมเมอร์"
    def __init__(self , name , salary):
        super().__init__(name , salary , self.__DepartmentName) #ใช้กับConstructor
        self.ShowData()


class Sale(Employee):
    __DepartmentName = "ขาย"
    def __init__(self , name , salary):
        super().__init__(name , salary , self.__DepartmentName)


#crate object
Account = Accounting("FreeFire" , 20000)
programmer = Programmer("King" , 60000)


#Show data
Account.ShowData()
