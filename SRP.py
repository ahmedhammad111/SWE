# Single Responsibility Principle
class Calculator:
    def sum(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class ResultSaver:
    def save(self, result):
        print("Saved result to database")