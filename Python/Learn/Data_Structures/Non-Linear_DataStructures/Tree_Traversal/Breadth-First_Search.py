'''
Breadth-First Search(BFS) คือการสำรวจ Sibling Nodeให้ครบก่อน ก่อนที่จะขยับลงไป Nodeระดับถัดไป

    A
   / \
  B   C
 / \   \
D   E   F

A → B → C → D → E → F
'''

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return
    
    queue = deque([root]) #เพิ่มrootเข้าqueue

    while queue:
        node = queue.popleft()
        print(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#Create Tree

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.right = Node("F")