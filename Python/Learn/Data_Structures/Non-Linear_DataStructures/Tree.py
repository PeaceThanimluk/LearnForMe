# ===================================
# Tree
# ===================================
'''
Tree = โครงสร้างข้อมูลแบบต้นไม้(Tree Data Structure)ใช้เก็บข้อมูลแบบลำดับขัั้น(hierarchical)
คล้ายกับต้นไม้กลับหัว
เช่น folder ในคอมพิวเตอร์ / โครงสร้าง HTML,XMl / Ai,Search ALgorithms

โครงสร้างพื้นฐานของTree
Root = โหนดบนสุด
Node = จุดเก็บข้อมูล
Child = ลูกของNode
Parent = แม่ของNode
Leaf = node ปลายสุดไม่มีลูก

        A
       / \
      B   C
     / \
    D   E

A = Root
B,C = Child of A
D,E = child of B
D,E,C = Leaf

B,C = Sibling

ประโยชน์ของ Tree
1.Search เร็วมาก เช่น Binaary Search Tree
2.เก็บข้อมูลเป็นชั้นๆ เช่น Folder , Menu
3.Ai game 
4.Data Base 
'''

#ตัวอย่างโค้ด Tree 

class Node:
    def __init__(self, data):
        self.data = data
        self.Children = []

#Create Node(data)
root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

#ทำให้ b,c เป็น childrendของa
root.Children.append(b)
root.Children.append(c)

#ทำให้ d เป็นๅ Childrend ของ b
b.Children.append(d)


# ===================================
# Binary Tree
# ===================================
'''
Binary Tree คือ Tree ที่แต่ละ Node จะมี Child Node ได้มีเกิน 2 Node
โดย Child Node จะมี Left Child และ Right Child

ประเภทของ Binary Tree 
1.Full BInary Tree
ทุก Node จะมีลูก 0 หรือ 2 คน เท่านั้น ไม่มี1
    A
   / \
  B   C
 / \
D   E

2.Complete Binary Tree
ต้นไม้ที่มีNodeเต็มทุกชั้น ยกเว้นชั้นล่างสุดที่ต้องเรียงจากซ้ายไปขวา ช่องสุดท้ายอาจไม่เต็มได้

    A
   / \
  B   C
 / \ /
D  E F

3.Perfect Binary Tree
ทุกชั้นเต็มหมด และ leaf อยู่ระดับเดียวกัน

      A
    /   \
   B     C
  / \   / \
 D  E  F  G

 4.Balance Binary Tree
 Binary Tree ที่ถูกออกแบบมาเพื่อป้องกันไม่ให้ต้นไม้เอียงจนเกินไป
 ต้นไม้ที่ความสูงของกิ่งซ้ายและกิ่งขวาของทุกๆNodeแตกต่างกันไม่เกิน1ชั้น

      20
    /  \
   10   30
       /  \
      25  40

'''

