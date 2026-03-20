"""
Composition คือ objectหนึ่งประกอบขึ้นจากobjectอื่น
เป็นการเอาของหลายชิ้นมาประกอบเป็นตัวเดียว เช่น รถ = ล้อ + เครื่องยนต์ + เบรก 
"""

class Engine:
    def __init__(self , horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self , size):
        self.size = size

class Car:
    def __init__(self , make , model , horse_power , wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power) #เรียกใช้class engine 
        self.Wheel = [Wheel(wheel_size) for wheel in range(4)] #ใช้class wheel 4ครั้ง

    def Display_Car(self):
        return f"{self.make} {self.model}"
    
car = Car(make = "Ford" , model = "Mustang" ,horse_power = 500 ,wheel_size = 18 )
print(car.Display_Car())