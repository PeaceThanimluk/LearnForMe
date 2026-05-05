'''
Queues หลักการทำงานคือ FIFO(First in, First Out) เข้าก่อน ออกก่อน
เหมือนกับการเข้าแถวซื้อของ ใครมาก่อนก็ได้บริการก่อน

Queuesเอาไปทำอะไรได้บ้าง
1.Task Scheduling
2.การจัดการคิวในระบบคอมพิวเตอร์

วิธีการใช้งานใน python คือจะใช้ library จาก python
'''

from collections import deque

#สร้างqueue
queue = deque()

#1.การใส่ข้อมูล(Enqueue)
queue.append("คนแรก")
queue.append("คนที่สอง")
queue.append("คนที่สาม")

#2.ดึงข้อมูล(Dequeue) -ดึงตัวแรกที่เข้ามาออก
First_In = queue.popleft()



