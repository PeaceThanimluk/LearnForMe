#Abstraction = คือการซ่อนรายละเอียดการทำงานที่ซับซ้อน
#เปิดเผยแค่interfaceที่จำเป็น
'''
ประโยชน์ของ abstract class คือ
-ลดความซับซ้อน ช่วยให้user หรือ programmer คนอื่นโฟกัสเฉพาะส่วนที่จำเป็น
-สร้างมาตราฐาน: บังคับให้child class ต้องมี Methodตามที่กำหนดไว้(Blueprint)
-บำรุงรักษาง่าย: แก้ไขcodeเบื้องหลังได้โดยไม่กระทยกับคนที่เรียกใช้งาน
'''
#ใช้โดย import module abc(Abstract Base Class)

from abc import ABC, abstractmethod

#สร้าง Abstract Class(แม่พิมพิ์)โดยใช้ ABC
class Vehicle(ABC):

    @abstractmethod #สร้าง abstract method(methodแม่พิมพิ์)
    def go(self): #สร้าง method abstract ให้กับ class
        pass #ภายในabstract method จะต้องไม่มีอะไร(implement) ให้chlid class ไปปรับแต่งเอาเอง
#abstractmethod บังคับให้ต้องให้ SubClass ต้องใส่ method ที่abstract ถ้าไม่ใส่จะ error
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle): #สร้างSubClassของ Vehicle class(abstract class)

    def go(self):
        print("You drive the car!")
    
    def stop(self):
        print("You stop the car!")

car = Car()

car.go()