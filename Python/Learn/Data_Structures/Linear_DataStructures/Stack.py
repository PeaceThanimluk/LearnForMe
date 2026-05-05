'''
Stack = หลักการทำงานคือ LIFO(Last in , First Out) เข้าทีหลังออกก่อน
เหมือนกับการวางจาานซ้อนกัน จานใบที่วางลงไปล่าสุด จะต้องถูกหยิบออกมาก่อนเสมอ

ประโยชน์ของStack
1Undo/Redo ในโปรแกรม Text editor
2.Function Call Stack
'''

#สร้างStackโดยใช้ List

stack = []

#ใส่ข้อมูล(Push)
stack.append("Web1")
stack.append("Web2")
stack.append("Web3")

#ดึงข้อมูลออกมา(Pop)ดึงตัวล่าสุด
LastItem = stack.pop() #Web3

