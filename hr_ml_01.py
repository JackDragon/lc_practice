# Enter your code here. It should call run_test(csv_path).
# import pandas as pd
# class TableLoader:
#     def __init__():
#         self.csv = None
#     def load_file(self, path):
#         self.csv = pd.read_csv(csv_path)
#     def compute():
#         if not self.csv:
#             return None
#         for col_name, col in self.csv.iteritems():
#             print("{}: mean {}, median {}, stdev {}".format(col_name, col.mean(), col.median(), col.std()))
import csv
from collections import defaultdict
import math
class TableLoader:
    def __init__(self):
        self.data = None
    # Load the file into a dict with indices as the column number.
    # Each item in the dict has a "name" and a list of "values."
    def load_file(self, path):
        with open(path, "r") as f:
            self.data = defaultdict(dict)
            reader = csv.reader(f)
            # Assume the csv is split by commas
            headers = reader.next()#.split(",")
            print(headers)
            for index, header in enumerate(headers):
                self.data[index] = {'values':[], 'name':header}
                # print(index, str(self.data[index]))
            for row in reader:
                for index, value in enumerate(row):
                    self.data[index]['values'].append(float(value))
            print(str(self.data))
    def compute(self):
        if not self.data:
            return None
        for column in self.data.values():
            sorted_data = sorted(column['values'])
            total = sum(sorted_data)
            length = len(column['values'])
            mean = total/length
            # This median works for odd and even lengths
            median = (sorted_data[(length-1)//2] + sorted_data[length//2])/2
            stdev = 0
            for value in sorted_data:
                stdev += (mean-value)*(mean-value)
            stdev = math.sqrt(stdev/length)
            print("{}: mean {}, median {}, stdev {}".format(column['name'], mean,median,stdev))
loader=TableLoader()
loader.load_file("data.csv")
loader.compute()