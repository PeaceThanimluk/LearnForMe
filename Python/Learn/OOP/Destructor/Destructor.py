'''
Destructor จะตรงข้ามกับConstructor
จะถูกใช้งานเมื่อสิ้นสุดการทำงานของclass หรือถูกทำก่อนจะสลายobject
ส่วนใหญ่จะเป็นหลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ

โครงสร้าง Destructor
def __del__(self):
    pass

'''

#Constructor ใช้งานเมื่อเริ่มต้นสร้างวัตถุ
'''โครงสร้างConstructor
def__init__(self):
    pass
'''

class Employee:

    def __init__(self , name , salary): #Constructor 
        self.name = name
        self.salary = salary
    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.name))
        print("Salary = {}".format(self.salary))
    
    def __del__(self): #Destructor
        print("call Destructor")
    

obj1 = Employee("peace" , 10)
obj1.salary = 1000 #เปลี่ยนค่าobjได้
obj2 = Employee("monk" , 100)
obj1.ShowData()
obj2.ShowData()