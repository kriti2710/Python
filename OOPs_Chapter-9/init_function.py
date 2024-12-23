class Student:
    college_name = "PPSU"
    # default constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, name, marks):
        self.name=name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("Kriti", 98)
print(s1.name, s1.marks)
s2 = Student("Liza", 97)
print(s2.name, s2.marks,s2.college_name)