class Calculator:
    def __init__(self, a, b):
       self.a = a
       self.b = b
        
    def operate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "sub":
            return self.a - self.b
        elif operation == "mul":
            return self.a *  self.b
        elif operation == "div":
            return self.a /  self.b if self .b != 0 else "Error: Division by Zero"
        else:
            return "Invalid operation"
        calc =Calculator(10, 5)
        
        print(calc.operate("add"))
        
        
        