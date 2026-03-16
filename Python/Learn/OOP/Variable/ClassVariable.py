#Class Variable = ตัวแปรที่ทำงานภายใน class ส่วนอื่น สามารถเข้าถึงข้อมูลส่วนนี้ได้เลย โดยไม่จำเป็นต้องสร้างobject ขึ้นมา
#เอาไว้เก็บค่าที่object ข้อมูลเหมือนกัน
#เอาไว้ใช้นับจำนวน
#เอาไว้เก็บค่าคงที่

class Employee:
    #Class Variable
    _minSalary = 12000
    _MaxSalary = 50000
    _CompanyName = "SixSevenCompany"
    def __init__(self , name , salary): 
       #Instance Variable
        self.__name = name
        self.__salary = salary

    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))
    
#Create Object
obj1 = Employee("peace" , 10)
print(Employee._CompanyName)