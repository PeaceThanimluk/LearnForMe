#Duck typing เป็นแนวคิดที่ว่า เราไม่สนว่าตัวแปรเป็นClassอะไร
#ขอแค่ใช้งานได้เหมือนกัน

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:
    def speak(self):
        print("Honk!")

animalLiast = [Dog() , Cat() , Car()] #สนใจแค่ว่ามี method ที่ชื่อว่า speakไหม

for animal in animalLiast:
    animal.speak()