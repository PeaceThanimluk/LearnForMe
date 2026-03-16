"""
Inheritance คือการสร้างสิ่งใหม่ด้วยการสืบทอดหรือรับเอาคุณสมบัติบางอย่าง
มาจากสิ่งเดิมที่มีอยู่แล้วโดยการสร้างเพิ่มเติมจากสิ่งที่มีอยู่แล้วได้เลย

ข้อดีของการinheritance คือ จากการที่สามารถนำสิ่งที่เคยสร้างขึ้นแล้วนำกลับ
มาใช้ใหม่(reuse)ได้ ทำให้ช่วยประหยัดเวลาการทำงานลงเนื่องจากไม่ต้องเสีย
เวลาพัฒนาใหม่หมด

Super class
Sub class
"""

class Employee: #SuperClass
    #Variables
    MinSalary = 12000
    MaxSaraly = 50000
    _CompanyName = "SixSevenCompany"
    __Private = "Baka"


    def __init__(self , name , salary): 
       #Instance Variable
        self.__name = name
        self.__salary = salary

    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))

#SubClass
class Accounting(Employee): #Inheritance
    def __init__(self):
        pass

class Programmer(Employee):
    def __init__(self):
        pass


class Sale(Employee):
    def __init__(self):
        pass


#crate object
Account = Accounting()
programmer = Programmer()
sale = Sale()

#Output
print(Account.MaxSaraly) #สามารถนำข้อมูลของclass employee(SuperClass) มาใช้ได้
#วิธีเอาข้อมูลProtected ของ SuperClass มาใช้
print(programmer._CompanyName)
