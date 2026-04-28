# ===================================
# Binary Search Tree
# ===================================
'''
Binary Search Tree(BST) = Binary Tree ที่จัดเรียงตามข้อมูลตามกฏเฉพาะ

////กฏของBST//////
-ค่าฝั่งซ้าย น้อยกว่า Node ปัจจุบัน
-ค่าฝั่งขวา มากกว่า Node ปัจจุบัน

        8
      /   \
     3     10
    / \      \
   1   6      14
      / \     /
     4   7   13

////ประโยชน์ของBinary Search Tree////
1.Search เร็ว
2.Insert ข้อมูลแบบเรียงอัตโนมัติ
3.Delete Data  = ลบ Node ได้โดยยังรักษากฏของ BST
4.เรียงข้อมูล
5.ใช้จริงในระบบ เช่น Dictionary , Database Index , Ranking System

'''

#Create Node
class Node:
    def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None

#Insert
def Insert(root, value):
    if root is None:
        return Node(value) #ถ้าTreeนั้นยังไม่มีRoot จะให้Nodeนั้นเป็นRootแทน

    if value < root.value: #ถ้าNodeนั้นมีค่าน้อยกว่า Root จะให้ไปอยู่ Left Child 
        root.left = Insert(root.left, value)
    elif value > root.value: #ถ้าNodeนั้นมีค่ามากกว่า Root จะให้ไปอยู่ Right Child
        root.right = Insert(root.right, value)

    return root

#Search

def Search(root, target):
    if root is None:
        return False
    
    if root.value == target:
        return True
    
    if target < root.value: #ถ้าtargetมีค่าน้อยกว่าNodeนั้น จะให้ทำซ้ำกับFunctionแต่จะเปลี่ยนเป็น Left Child แทน
        return Search(root.left, target)
    else:
        return Search(root.right, target) #ถ้าTargetมีค่ามากกว่าNodeนั้น จะให้ทำซ้ำกับFunctioncแต่จะเปลี่ยนเป็น Right Child แทน
