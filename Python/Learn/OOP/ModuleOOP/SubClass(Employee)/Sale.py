from employee import Employee #ต้องอยู่ในfolderเดียวกันถึงจะimportได้
class Sale(Employee):
    __DepartmentName = "ขาย"
    def __init__(self , name , salary , area):
        super().__init__(name , salary , self.__DepartmentName)
        self.area = area

    def ShowData(self): #Overriding method ชื่อ method เหมือนกันแต่ทำงานต่างกัน ขึ้นอยู่กับSubClass
        super().ShowData()
        print(f"Area = {self.area}")