class Student:

    def __init__(self , name):
        self.name = name
        self.__score = 0
        

    def add_score(self , score):
        if isinstance(score , int) and score >= 0:
            self.__score += score
        else:
            print("Invalid value")

    def get_score(self):
        return self.__score
    
    def get_grade(self):   
            if self.__score >= 80:
                return "A"
            elif self.__score >= 75:
                return "B+"
            elif self.__score >= 70:
                return "B"
            elif self.__score >= 65:
                return "C+"
            elif self.__score >= 60:
                return "C"
            elif self.__score >= 55:
                return "D+"
            elif self.__score >= 50:
                return "D"
            else:
                return "F"
    
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.__score}")
        print(f"Grade: {self.get_grade()}")

s1 = Student("John")

s1.add_score(30)
s1.add_score(45)

s1.show_info()