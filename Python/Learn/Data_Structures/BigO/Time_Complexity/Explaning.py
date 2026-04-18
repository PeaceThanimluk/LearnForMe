#1.o(1) Constant Time
#ใช้เวลาเท่าเดิมเสมอ ไม่ว่าข้อมูลจะเยอะขนาดไหน

def get_first(my_list):
    return my_list[0]

#2.O(log N) Logarithmic Time
#ข้อมูลเพิ่มขึ้น2เท่า เวลาเพิ่มนิดเดียว มักใช้กับBinay Search

def binary_search(arr , target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

#3.O(n) Linear Time
#วนครบทุกข้อมูล ถ้ามี100ตัว ทำ100รอบ

arr = [1,2,3,4,5]

for x in arr:
    print(x)

#4.O(nlog n) Linearithmic
#ใช้ใน Merge Sort
'''
Merge Sort = แบ่งครึ่งข้อมูลไปเรื่อยๆ จนข้อมูลเหลือ1ตัวแล้วค่อยรวมกลับมาแบบเรียงลำดับ



'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 #หาตัวตรงกลาง

    left = merge_sort(arr[:mid]) #(Left Part) หยิบข้อมูลตั้งแต่ตัวแรกจนถึงก่อนตัวกลาง
    right = merge_sort(arr[mid:]) #(Right Part) หยิบข้อมูลตั้งแต่ตำแหน่งตัวกลางจนจบlist

    return merge(left,right)

def merge(left, right):
    result = []
    i = j = 0 #i= index ของ left / j=index ของ right


    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:]) #เอาสมาชิกที่เหลืออยู๋ต่อท้าย
    result.extend(right[j:])

    return result





