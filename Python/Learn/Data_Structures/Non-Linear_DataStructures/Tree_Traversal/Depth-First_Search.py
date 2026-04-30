'''
Depth-First Search(DFS) เป็นการเดินสำรวจข้อมูลแบบลึกก่อน ไปให้ลึกที่สุดก่อนค่อย backtrack

    A
   / \
  B   C
 / \
D   E
เช่น A->B->D->E->C
DFS ใช้ทำอะไรได้บ้าง
-ค้นหาNode ใน Graph
-ตรวจสอบว่า Graph เชื่อมถึงกันไหม
-หา Path

DFS มี 3 รูปแบบคือ
1.Pre-Prder(Root->Left->Right) มักใช้เพื่อคัดลอกโครงสร้างTree
2.In-Order(Left->Root->Right) มักใช้เพื่ให้ได้ข้อมูลเรียงลำดับจากน้อยไปมาก
3.Post-Order(Left->Right->Root) มักใช้เพื่อลบ Tree หรือ คำนวณขนาดของ Tree

'''

###SET-UP###
'''
    A
   / \
  B   C
 / \   \
D   E   F
   / \
   G  H

'''
class Node:
    def __init__(self , value):
         self.value = value
         self.left = None
         self.right = None
         
Root = Node("A")
Root.left = Node("B")
Root.right = Node("C")

Root.left.left = Node("D")
Root.left.right = Node("E")

Root.right.right = Node("F")

Root.left.right.left = Node("G")
Root.left.right.right = Node("H")

'''
    A
   / \
  B   C
 / \   \
D   E   F
   / \
   G  H

'''

# ===================================
# 1.Pre-Order (Root->Left->Right)
# ===================================

def Pre_Order(root):
    if root:
        print(root.value,end="->")
        Pre_Order(root.left)
        Pre_Order(root.right)

print("Pre-Order")
Pre_Order(Root)
print("")
        
#OUTPUT = A->B->D->E->G->H->C->F->

# ===================================
# 2.In-Order (Left-Root-Right) หาตัวซ้ายล่างสุดก่อน หลังจากนั้นจะย้อนกลับไปrootแล้วright
# ===================================

def In_Order(root):
    if root:
        In_Order(root.left)
        print(root.value,end = "->")
        In_Order(root.right)

#OUTPUT = D->B->G->E->H->A->C->F->

print("In-Order")
In_Order(Root)
print("")

# ===================================
# 3.Post-Order (Left-Right-Root)
# ===================================

def Post_Order(root):
    if root:
        Post_Order(root.left)
        Post_Order(root.right)
        print(root.value , end="->")

print("Post-Order")
Post_Order(Root)

#OUTPUT = D->G->H->E->B->F->C->A->