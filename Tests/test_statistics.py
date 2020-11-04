import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from CsvReader.CsvDataAppend import data_add


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/StatCalcData.csv')

    # Mean
    def test_Population_Mean_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.mean(lst), float((column['mean'])))
            self.assertNotEqual(self.statistics.mean(lst), float((column['mean'])) * 2, "Mean does not match")

    # Median
    def test_Median_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.med(lst), float((column['median'])))
            self.assertNotEqual(self.statistics.med(lst), float((column['median'])) + 2, "Incorrect Median")


if __name__ == '__main__':
    unittest.main()
