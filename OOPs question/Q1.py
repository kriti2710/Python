#  to create a calculator by using arithmetic operations

class Calculator:
    def add(self, a,b):
        return a + b
    
    def sub(self, a,b):
        return a - b
    
    def mul(Self, a, b):
        return a * b
    
    def div(self, a,b):
        if b != 0:
            return a/b
        else:
            print("cannot divide by zero")
    
cal1 = Calculator()
print("25+5 =",cal1.add(25,5))
print("25-5 =",cal1.sub(25,5))
print("25*5 =",cal1.mul(25,5))
print("25/5 =",cal1.div(25,5))

