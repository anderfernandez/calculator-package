from calculator.calculator import Calculator
from calculator.teacher.teacher import Teacher

def test_explain_procedure():
    teacher = Teacher()
    calculator = Calculator()

    # Test addition
    explanation = teacher.explain_procedure(2, 3, "+")
    assert "Add 2 and 3 to get 5." in explanation

    # Test subtraction
    explanation = teacher.explain_procedure(5, 2, "-")
    assert  "Subtract 2 from 5 to get 3." in explanation

    # Test multiplication
    explanation = teacher.explain_procedure(4, 6, "*")
    assert "Multiply 4 and 6 to get 24." in explanation

    # Test division
    explanation = teacher.explain_procedure(10, 2, "/")
    assert "Divide 10 by 2 to get 5." in explanation



test_explain_procedure()
