#Setter คือMethodกำหนดค่าให้object Private 
#Getter คือMethodก่ีดึวค่าของobject  Private

class Employee:

    def __init__(self , name , salary): 
        #Public Attribute
        self.__name = name
        self.__salary = salary

    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))

    def setName(self , newname): #Function to change name in class(private)
        self.__name = newname

    def setSalary(self , newSalary): #Function to change Salary data(private)
        self.__salary = newSalary
    
    def getName(self): #get attribute from object
        return self.__name

#Create Object
obj1 = Employee("peace" , 10)
obj2 = Employee("monk" , 100)

#change new name by using setName function
obj1.setName("Skibidy")

#Change new salary by using setSalary function
obj1.setSalary(1030)

#Show data
obj1.ShowData()

#show attribute of object
print(obj1.getName())