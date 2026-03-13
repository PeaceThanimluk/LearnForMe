#dir แสดงattribute และ Method

class Employee:

    def __init__(self , name , salary): 
        self.name = name
        self.salary = salary
    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.name))
        print("Salary = {}".format(self.salary))
    

obj1 = Employee("peace" , 10)
obj2 = Employee("monk" , 100)

print(dir(obj1))

#เช็คว่าobjectมาจากclassอะไร
print(obj1.__class__)