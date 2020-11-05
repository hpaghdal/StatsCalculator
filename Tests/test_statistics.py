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

    # Mode
    def test_Mode_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.mod(lst), float((column['mode'])))
            self.assertNotEqual(self.statistics.mod(lst), float((column['mode'])) - 2, "Incorrect Mode")

    # Standard Deviation
    def test_Population_Standard_Deviation_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.stddev(lst), float((column['stdev'])))
            self.assertNotEqual(self.statistics.stddev(lst), float((column['stdev'])) * 3, "Wrong Pop Std Deviation")

    # Z-Score
    def test_zscore_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.z_score(lst), float((column['zscore'])))
            self.assertNotEqual(self.statistics.z_score(lst), float((column['zscore'])) * 2, "Incorrect Z Score")

    # Variance
    def test_population_variance_calculator(self):
        test_data = CsvReader('Tests/Data/StatCalcData.csv').data
        answer = CsvReader('Tests/Data/StatAnswers.csv').data
        lst = data_add(test_data)
        for column in answer:
            self.assertEqual(self.statistics.pvariance(lst), float((column['pop_variance'])))
            self.assertNotEqual(self.statistics.pvariance(lst), float((column['pop_variance'])) - 3, "Wrong Pop Var")






if __name__ == '__main__':
    unittest.main()
