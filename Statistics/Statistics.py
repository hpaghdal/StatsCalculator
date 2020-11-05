from Calculator.Calculator import Calculator
from CsvReader.CsvReader import CsvReader
from Statistics.PopulationMean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import st_dev


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
    # Mode
    def mod(self, a):
        self.result =mode(a)
        return self.result
    # Standard Deviation
    def stddev(self, a):
        self.result = st_dev(a)
        return self.result



