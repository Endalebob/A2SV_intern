'test_arthimetic_operations.py'
import pytest
from arithmetic_operations import ArthimeticClass

class TestArithmeticClass:
    def test_add(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.add(x, y)
        # assert
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", 2)
        with pytest.raises(TypeError):
            ArthimeticClass.add(1, "2")
        with pytest.raises(TypeError):
            ArthimeticClass.add("1", "2")
        
        assert expected_output == actual_output
        
  
'arthimetic_operations.py'
# This class does arithmetic operations
class ArthimeticClass:
    def add(x, y):
        # adding two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both inputs should be numbers")
        return x + y
    def subtract(x, y):
        # subtracting two numbers
        return x - y
    def multiply(x, y):
        # multiplying two numbers
        return x * y
    def divide(x, y):
        # dividing two numbers
        return x / y