class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((self.phy + self.chem + self.maths) /3) + "%"
    
    def calPercentage(self):
        self.percentage = str((self.phy + self.chem + self.maths) /3) + "%"
stud1 = Student(97,98,99)
print(stud1.percentage)

stud1.phy = 86
print(stud1.phy)
print(stud1.percentage)
stud1.calPercentage()
print(stud1.percentage)