#Linked list คือ โครงสร้างข้อมูลที่เก็ลข้อมูลเป็นNode ต่อกันเป็นสายโซ๋
#โดยแต่ละnodeจะมี 1.data/value 2.ตัวชี้ไปยังโหนดถัดไป(next)

'''
ข้อดีของ Linked List
1.สามารถแทรกข้อมูลใหม่ลงในตำแหน่งที่ต้องการได้โดยไม่ต้องกังวลเรื่องการขยับตำแหน่งข้อมูลอื่น
2.ขยายขนาดง่าย

ข้อเสียของ Linked List
1.ถ้าถึงindexช้า เช่น จะเอาตัวที่100ต้องไล่ทีละตัวO(n)
2.ใช้memoryเพิ่ม เพราะแต่ละnodeต้องเก็บค่าnext

โดยLinked list จะมีทั้งหมด4แบบ
'''

#1.Singly Linked List(listแบบทิศทางเดียว) แต่ละnodeจะมีpointerชี้ไปยังnodeถัดไปเพีบงทิศทางเดียวเท่านั้น
#จากหน้าไปหลัง ไม่สามารถย้อนกลับได่ จุดสิ้นสุดของnodeจะชี้ไปที่ NONE 10->20->30->None
#ข้อดีคือใช้ Memoryน้อย ข้อเสียคือ ไม่สามารถย้อนกลับและวนลูปได้

# ===================================
# 1)Single Linked List
# ===================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#สร้าง node 
a = Node(10)
b = Node(20)
c = Node(30)

#สร้างpointer
a.next = b
b.next = c

head = a #กำหนดว่าให้aเป็นลำดับแรก

current = head
while current:
    print(current.data)
    current = current.next #เปลี่ยนลำดับถัดไป

#2.Doubly Linked list(Listแบบสองทิศทาง) จะมีpointer 2 ตัว คือชี้ไปทั้ง Next Node และ Previous Node
#จุดเด่น : สามารถเดินหน้าและถอยหลังได้ ใช้ทำ Browser Back/Forward Page , Undo/Redo , Music Playlist
#ข้อเสีย : ใช้หน่วยความจำเพิ่มมากขึ้นเพราะจะต้องเก็บpointerเพิ่มอีก1ตัวในแต่ละNode

# ===================================
# 2)Doubly Linked List
# ===================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.prev = a

b.next = c
c.prev = b

head = a

#เดินหน้า
current = head
while current:
    print(current.data)
    last = current
    current = current.next
    #last คือตัวมันเอง / ตัวก่อนของตัวถัดไป
    #current = ตัวข้างหน้าของlast / ตัวปัจจุบัน

#ถอยหลัง
current = last
while current:
    current = current.prev

#3.Circular Singly Linked List(Listแบบวงกลม) คือการนำ singly Linked List หรือ Doubly Linked List มาเชื่อมต่อกันจนเป็นวงกลม
#โดยให้Nodeสุดท้ายกลับมาที่Nodeแรก
#จุดเด่น : ไม่มีจุดสิ้นสุด ทำให้สามารถวนลูปใช้งานรายการได้อย่างต่อเนื่องไม่รู้จบ
#การใช้งาน : เหมาะกับงานที่ต้องการวนรอบ เช่น การจัดการคิวงานในรบบ operating system ที่ให้ cpu ประมวลผล

'''
10 → 20 → 30
↑         ↓
└─────────┘
'''

# ===================================
# 3)Circular Singly Linked List
# ===================================

class Node:
    def __init__(self, data):
         self.data = data
         self.next = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c
c.next = a

head = a
current = head

for _ in range(6): #วนดู6ครั้ง
    print(current.data)
    current = current.next

#4.Circular Doubly Linked List(Listแบบวงกลมสองทิศทาง) Nodeสุดท้ายชี้กลับมาที่ Nodeแรก ด้วย Next Nodeแรกชี้ไปที่ Nodeสุดท้ายด้วย Prev
#จุดเด่น : มี2ทิศทาง ไปข้างหน้าและถอยหลังได้ เช่น สร้างระบบ playlist music ที่มี next , previous ระบบคัดเลือกคิวงาน
#ข้อเสีย : ใช้memory มากกว่า ลบ nodeง่าย
'''
10 ⇄ 20 ⇄ 30
↑         ↓
└─────────┘
'''

# ===================================
# 4)Circular Doubly Linked List
# ===================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.prev = a 

b.next = c
c.prev = b

a.prev = c
c.next = a

head = a
current = head

#Forward
for _ in range(6):
    print(current.data)
    current = current.next

#Backward
current = head
for _ in range(6):
    print(current.data)
    current = current.prev