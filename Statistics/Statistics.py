from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from Statistics.PopulationMean import mean
from Statistics.Median import median


class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/StatCalcData.csv').data
        super().__init__()

    # Mean
    def mean(self, a):
        self.result = mean(a)
        return self.result
    # Median
    def med(self, a):
        self.result = median(a)
        return self.result

