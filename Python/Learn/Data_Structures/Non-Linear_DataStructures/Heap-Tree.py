'''
Heap Tree คือโครงสร้างข้อมูลรุปแบบ Binary Tree มีกฏในการเรียงลำดับNode
เพื่อให้เราสามารถเข้าถึงค่าที่ มากที่สุด หรือ น้อยที่สุด ได้อย่างรวดเร็ว

1.Max-Heap = Parent Node จะต้องมีค่ามากกว่าหรือเท่ากับ Child Node เสมอ ค่าRootจะมากสุดเสมอ
2.Min-Heap = Parent Node จะต้องมีค่าน้อยกว่าหรือเท่ากับ Child Node เสมอ Root จะมีค่าน้อยที่สุดเสมอ

ประโยชน์ของHeap
-ใช้เวลาเร็วและใช้พื้นที่น้อยกว่าการใช้ List.sort()
-Priority Queue เรียงลำดับความสำคัญ ช่วยให้เราเลือกจัดการกับงานที่ สำคัญที่สุดก่อนเสมอ ไม่ว่างานนั้นจะถูกส่งมาเมื่อไร
-หาค่า K-Largest หรือ K-Smallest (ค่าที่มากที่สุดหรือน้อยที่สุดในลำดับที่K)
-Graph Algorithm -> Dijkstra’s Algorithm หาเส้นทางที่สั้นที่สุดโดยใช้ Mini-Heap
'''

#ใช้ Libraly heapq

import heapq

#Create List
data = [10,1,5,20,3]

print(f"Old Data : {data}")

#แปลงListให้กลายเป็นHeap(Mini-Heap)
heapq.heapify(data)

print(data)

#Add New Data
heapq.heappush(data , 0)

#Get Smallest data
smallest = heapq.heappop(data)
print(f"Smallest Value : {smallest}")