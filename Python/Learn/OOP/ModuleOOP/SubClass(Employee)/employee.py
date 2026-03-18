#การสร้างClass แบบแยกไฟล์

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