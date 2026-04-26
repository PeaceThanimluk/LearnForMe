#1.O(1) Constant Space = การที่โปรแกรมคงที่ ไม่ว่าข้อมูลนำเข้าจะมากมายแค่ไหน

def add(a,b):
    return a + b

#2.O(n) Linear Space = คือการที่โปรแกรมใช้พื้นที่เพิ่มขึ้นเป็นเส้นตรง ตามขนาดของข้อมูล
#เช่นการสร้าง List หรือ Dictionary

def create_list(n):
    return [i for i in range(n)] #สร้าง list ที่มีตัวเลขตั้งแต่0 ถึง n-1
    '''
    list = []
    for i in range(n):
    list.append(i)
    return list

    ตัวอย่างการใช้
    create_list(5)
    ผลลัพธ์ = [0,1,2,3,4]
    '''

#3.O(n^2) Quadratic Space = มักใช้สร้าง ตาราง matrix หรือทำ nested loop

def create_matrix(n):
    return [[0 for j in range(n)] for i in range(n)] #สร้าง matrixขนาด nxn ที่ทุกช่องมีค่าเป็น0
    '''
    เขียนแบบธรรมดา
    def create_matrix(n):
        matrix = []

        for i in range(n): วงนอก : สร้างแถวข้างบนจำนวนnครั้ง
            row = 
            for j in range(n): วงใน : สร้าง list ที่เป็นเลข0จำนวนnช่อง
                row.append(0)

            matrix.append(row)

        return matrix

        เช่น create_matrix(2)
        [
            [0,0],
            [0,0]
        ]
        จะได้เป็น matrix2x2
    '''

#4.O(logn) Logarithmic Space มักพบใน algorithm ประเภท recursive(fucntionเรียกใช้งานตัวเอง)เช่น Binary Research
def binary_search(arr, left, right, target):
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

