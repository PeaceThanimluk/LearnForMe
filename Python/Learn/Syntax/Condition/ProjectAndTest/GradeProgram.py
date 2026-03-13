score = int(input("Your test score : "))
Grade = None

print("Your test score is : " , score)

if score >= 80 and score <= 100:
    Grade = "A"
elif score >= 70 and score <= 79:
    Grade = "B"
elif score >= 0 and score <= 69:
    Grade = "F"
else:
    Grade = "Your score is too low or too high!"

print("Your is grade is : " , Grade)