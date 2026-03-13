class Employee:
    def details(self , name , salary): #Function to set data
        self.name = name
        self.salary = salary
    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.name))
        print("Salary = {}".format(self.salary))
    

emp1 = Employee() #Create object
emp1.details("Six Seven" , 10000) #Set data

emp2 = Employee()
emp2.details("Skibidy" , 20000)
