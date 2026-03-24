#Class Method มีหน้าที่เข้าถึงตัวแปรของclass
"""
ประโยชน์ของclass method 
-ใช้นับจำนวนobjectที่ถูกสร้าง
-ใช้เข้าถึงตัวแปรของclass
-ช่วยให้codeเป็นระเบียบมากขึ้น
"""
#cls = ตัวแทนของclass (เหมือนselfแต่ของclass)


#ตัวอย้่างที่1

class Myclass:
    count = 0

    def __init__(self):
        Myclass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

Myclass.get_count()

#ตัวอย่างที่2

class Player:
    total = 0

    @classmethod
    def add_player(cls):
        cls.total += 1

