import numpy as np
import csv

class Matrix:
    def __init__(self, PATH):
        self.algorithms = []
        self.criteria = []
        numeric_data = []

        with open(PATH, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.criteria = header[1:]

            for row in reader:
                self.algorithms.append(row[0])
                numeric_data.append([float(x) for x in row[1:]])

        self.matrix = np.array(numeric_data)

    def print(self):
        print("Matrix: ")
        print(f"Criteria: {self.criteria}")
        print(f"Algorithms: {self.algorithms}")
        print(self.matrix, '\n')

    def get_matrix(self):
        return self.matrix
