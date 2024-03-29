import requests

from calculator.calculator import Calculator

class Teacher:
    def __init__(self):
        
        resp = requests.get("https://google.com")
        self.calculator = Calculator()


    def explain_procedure(self, num1: float, num2: float, operation: str) -> str:
        """
        Explain the procedure to get the result of a mathematical operation.

        Args:
            num1 (float): The first number.
            num2 (float): The second number.
            operation (str): The mathematical operation to perform.

        Returns:
            str: The explanation of the procedure.
        """
        explanation = f"Here's how to get the result of {num1} {operation} {num2}: "
        
        if operation == '+':
            explanation += f"Add {num1} and {num2} to get {self.calculator.add(num1, num2)}."
        elif operation == '-':
            explanation += f"Subtract {num2} from {num1} to get {self.calculator.subtract(num1, num2)}."
        elif operation == '*':
            explanation += f"Multiply {num1} and {num2} to get {self.calculator.multiply(num1, num2)}."
        elif operation == '/':
            explanation += f"Divide {num1} by {num2} to get {self.calculator.divide(num1, num2)}."
        else:
            explanation += "Invalid operation."

        return explanation
