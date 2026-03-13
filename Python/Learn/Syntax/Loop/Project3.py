Total = 0

while True:
    number = int(input("Type Number : "))
    if number <= 0:
        break
    Total += number
    
print("Finished! , Total = " , Total)