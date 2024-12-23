class Student:
    college_name = "PPSU"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome students", self.name, self.marks)

    def get_marks(self):
        return self.marks
    
s1 = Student("Kriti", 98)
s1.welcome()
print(s1.get_marks())
