import unittest
from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = CsvReader('Tests/Data/Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('Tests/Data/Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader('Tests/Data/Division.csv').data
        for row in test_data:
            x = float(row['Value 1'])
            y = float(row['Value 2'])
            z = float(row['Result'])
            self.assertEqual(self.calculator.divide(y, x), round(z, 7))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('Tests/Data/Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))