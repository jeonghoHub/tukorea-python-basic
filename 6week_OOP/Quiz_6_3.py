class Calc:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2
    def calculate(self, op):
        if op == '+':
            print(self.a, op ,self.b , '=' , self.a + self.b)
        else:
            print(self.a, op, self.b , '=', self.a * self.b)

num1 = int(input('Num1:'))
num2 = int(input('Num2:'))
obj = Calc(num1, num2)
obj.calculate('+')
obj.calculate('*')