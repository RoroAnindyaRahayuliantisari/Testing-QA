# Example code for unit testing in Python using the `unittest` module
import unittest

# Unit under test: A simple function to calculate the square of a number
def square(number):
    return number * number

# Test class
class TestSquare(unittest.TestCase):
    def test_square_positive_number(self):
        result = square(5)
        self.assertEqual(result, 25)

    def test_square_negative_number(self):
        result = square(-4)
        self.assertEqual(result, 16)

    def test_square_zero(self):
        result = square(0)
        self.assertEqual(result, 0)

# Run the tests
if __name__ == '__main__':
    unittest.main()