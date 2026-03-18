import unittest
from unittest.mock import patch

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        with patch('builtins.input', side_effect=['2', '3', '+']):
            with patch('builtins.print') as mock_print:
                import calculator
                mock_print.assert_any_call(5)

    def test_subtraction(self):
        with patch('builtins.input', side_effect=['5', '2', '-']):
            with patch('builtins.print') as mock_print:
                import calculator
                mock_print.assert_any_call(3)

    def test_multiplication(self):
        with patch('builtins.input', side_effect=['4', '6', '*']):
            with patch('builtins.print') as mock_print:
                import calculator
                mock_print.assert_any_call(24)

    def test_division(self):
        with patch('builtins.input', side_effect=['8', '2', '/']):
            with patch('builtins.print') as mock_print:
                import calculator
                mock_print.assert_any_call(4.0)

    def test_invalid_operation(self):
        with patch('builtins.input', side_effect=['1', '2', '^']):
            with patch('builtins.print') as mock_print:
                import calculator
                mock_print.assert_any_call('invalid operation')

if __name__ == '__main__':
    unittest.main()
