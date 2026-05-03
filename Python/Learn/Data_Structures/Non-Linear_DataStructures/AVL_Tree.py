'''
AVL Tree(Adelson-Velsky and Landis) คือ Self Balancing Binary Search Tree(BST)ชนิดหนึ่ง
ซึ่งความสูงของกิ่งด้านซ้าย(Left Child)และกิ่งด้านขวา(Right Child)จะต้องต่างกันไม่เกิน1เสมอ
ค่าความแตกต่างนี้เรียกว่า Balance Factor
Balance Factor = ความสูงทั้งหมดของกิ่งด้านซ้าย - ความสูงทั้งหมดของกิ่งด้านขวา
โดยค่าBF ที่ยอมรับได้ใน AVL Tree คือ -1 0 1 เท่านั้น หากมีการ Insert หรือ Delete ข้อมูลแล้วทำให้ ค่าเป็น >2 <-2 จะต้องมีการRotation
ตัวอย่างการคำนวณค่า Balance Factor
        3
       / 
      2
     /
    1
ค่าBFของ 1 คือ 0 เพราะไม่มีLeftChild RightChild
ค่าBFของ 2 คือ 1 เพราะ มี Left child สูง 1 Right Child สูง 0 1-0 = 1
ค่าBF ของ 3 คือ 2 เพราะ Left child สูง 2 Right Child สูง 0 2-0 = 2 
 
จากตัวอย่างจะเห็นว่า Balance Factor ไม่สมดุลเราจึงต้องทำการRotation

        2
     /    \
     3     1

ประโยชน์ของ AVL TREE
1.ใน Binary Tree ทั่วไป หากเราใส่ข้อมูลที่เรียงลำดับมาแล้ว ต้นไม้จะกลายเป็นเส้นตรง(Skewed Tree) ทำให้ความเร็วในการหาข้อมูลช้าลง
เหลือO(n) แต่ AVl จะบังคับ Rotation ให้สมดุล ทำให้ความเร็วคงที่ O(logn)
2.เหมาะกับงานค้นหา
'''

class TreeNode:
    def __init__(self , key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node: #ถ้าNodeนั้นไม่มีChild จะ return เป็น0
            return 0
        return node.height
    
    def get_balance(self , node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right) #เอาความสูงของLeft และ Right มาลบกันเพื่อหาค่า BF
    
    def rotate_right(self , y):
        x = y.left
        T2 = x.right #เก็บกึ่งขวาของ x ไว้ชั่วคราว
        '''
        y = Root ที่ไม่ ฺBalance
        x = Left Child ของ Root
        T2 =
        '''
        #Rotation
        x.right = y
        y.left = T2

        #Update Height
        y.height = 1 + max(self.get_height(y.left) , self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left) , self.get_height(x.right))
        return x
    
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        # ทำการหมุน
        y.left = x
        x.right = T2
        # อัปเดตความสูง
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def insert(self , root , key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

     # 4. ถ้าเสียสมดุล ให้จัดการตาม Case ต่างๆ
        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

# วิธีใช้งาน
tree = AVLTree()
root = None
keys = [10, 20, 30, 40, 50, 25]

for key in keys:
    root = tree.insert(root, key)   


        