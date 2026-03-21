#property decorator = เครื่องมือที่ช่วยให้เราเข้าถึง method ในclass
#ได้เมือนกับว่าเป็นattribute(ตัวแปร)
#ใช้ร่วมกับ setter , getter 
#มีlogic ตรวจสอบอยู่เบื้องหลัง
class BankAccount:
    def __init__(self):
        self._balance = 0 #ถ้าไม่ใส่_นำหน้า จะเกิดloopเพราะชื่อเดียวกับ @property

        @property
        def balance(self):
            return self._balance
        
        @balance.setter #logic เช็คค่าก่อนจะใส่
        def balance(self , value):
            if value < 0:
                raise ValueError("ติดลบไม่ได้")
            self._balance = value

acc = BankAccount()

acc.balance = -200
print(acc.balance)
