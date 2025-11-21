# calculator.py
class Calculator:
    def add(self, a, b):
        self._validate_input(a, b)
        return round(a + b, 2)

    def subtract(self, a, b):
        self._validate_input(a, b)
        return round(a - b, 2)

    def multiply(self, a, b):
        self._validate_input(a, b)
        return round(a * b, 2)

    def divide(self, a, b):
        self._validate_input(a, b)
        if b == 0:
            return "Error: Division by zero"
        return round(a / b, 2)

    def _validate_input(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Invalid input")