class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():  #by using static method we can call this method without using self parameter 
        print("hello")
        print("welcome")
    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("Kriti", [97,98,94])
s1.get_avg()
s1.name = "liza"
s1.get_avg()
s1.hello()
