#Static Method คือ methodธรรมดาที่อยู่ในclass เพื่อให้"เป็นหมวดหมู่"
#ไม่ผูกกับ object และไม่ใช่ self
#เหมาะกับfunction คำนวณ , helper function
class Math:
    @staticmethod
    def add(a , b):
        return a + b
    
result = Math.add(3 , 5)
print(result)