from  employee import Employee #ต้องอยู่ในfolderเดียวกันถึงจะimportได้

class Accounting(Employee): #Inheritance
    __DepartmentName = "บัญชี"
    def __init__(self , name , salary , age): #นำค่านำเข้าก่อน
        super().__init__(name , salary , self.__DepartmentName) #นำค่าที่ได้จากInitของAccountไปใส่ของEmployee
        self.age = age

    def ShowData(self): #Overriding method ชื่อ method เหมือนกันแต่ทำงานต่างกัน ขึ้นอยู่กับSubClass
        super().ShowData() #นำ method show data ของ SuperClass มาใช้ เพื่อแสดงผลข้อมูล name กับ salary ก่อน
        print(f"Age = {self.age}")