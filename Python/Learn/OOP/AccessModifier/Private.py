#วิธีการสร้างPrivate Attribute เราจะใช้เครื่องหมาย __ นำหน้าตัวแปร เช่น self.__name
#ถ้าเป็นPrivate attribute จะไม่สามารถกแก้ไขข้อมูลได้ ต้องแก้ไขภายในclassนั้นไ
class Employee:

    def __init__(self , name , salary): 
        #Public Attribute
        self.__name = name
        self.__salary = salary

    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))
    
#Create Object
obj1 = Employee("peace" , 10)
obj2 = Employee("monk" , 100)