#Access modifier คือระดับในการเข้าถึง class , attribute , Method มีประโยชน์ในเรื่องกำหนดสิทธิการเข้าถึง สิทธิในการใช้งาน
'''
public = ใครก็เข้าถึงได้
Protected = ระดับการเข้าถึงเฉพาะclassของตัวมันเองและcild class
วิธีการสร้างprotected คือ ใช้เครื่องหมาย_นำหน้าตัวแปรเช่น self._Name
Private = จะมีแต่class ของตัวมันเองเท่านั้นที่มีสิทธิ์ใช้งานได้

'''

class Employee:

    def __init__(self , name , salary): 
        #Public Attribute
        self.name = name
        self.salary = salary

    
    def ShowData(self): #Function use to show data
        print("Name = {}".format(self.name))
        print("Salary = {}".format(self.salary))
    
#Create Object
obj1 = Employee("peace" , 10)
obj2 = Employee("monk" , 100)