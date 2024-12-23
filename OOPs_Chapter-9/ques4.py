# define a Employee class with attributes role, department, salary. This class also has a showDetails() methods
# alsoo create an engineer class that inherits properties from Employee & has additional attributes: name & age
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print("role = ", self.role)
        print("department = ", self.department)
        print("salary = ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineering", "CSE", "95,000")

e1 = Employee("Accountant", "Finance", "60,000")
e1.showDetails()
eng = Engineer("kriti", 22)
eng.showDetails()
eng = Engineer("Ritika", 24)
eng.showDetails()