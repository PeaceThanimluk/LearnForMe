#วิธีการสร้างProtected Attribute เราจะใช้เครื่องหมาย _ นำหน้าตัวแปร เช่น self._name
#วิธีการจะใช้งานprotected attibute คือ ให้เขียนชื่อตัวแปรนั้นพร้อมกับเครื่องหมาย_นำหน้า แต่ต้องเป็นclass เดียวกัน
class Employee:

    def __init__(self , name , salary): 
        #Protected Attribute
        self._name = name
        self._salary = salary

    
    def _ShowData(self): #Function use to show data
        print("Name = {}".format(self._name))
        print("Salary = {}".format(self._salary))
    
#Create Object
obj1 = Employee("peace" , 10)
obj2 = Employee("monk" , 100)

#Change Protected Data
obj1._name = "sixSeven" 

#Show data 
obj1._ShowData()