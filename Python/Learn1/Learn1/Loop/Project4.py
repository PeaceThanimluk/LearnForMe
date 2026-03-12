Start = int(input("Multiplier Start : "))
End = int(input("Multiplier End : "))

for Number in range(Start , End + 1):
    print("Multiplier : " , Number) #Number = current index in Multiplier

    for Index in range(1 , 13): #Index = 1-12
        print(Number , "x" , Index , " = " , Number * Index)

    print("-------------")