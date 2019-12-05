import numpy as np
import pandas as pd


class CurrencyMatrix:
    currencies = []
    first_col = []
    first_line = []
    matrix = []

    def init(self):
        self.currencies = input(
            'Please enter the currencies you want to convert, each one followed by a space (the first one being the base one):\n>>\t').split(' ')
        self.first_col.append(1)
        self.first_line.append(1)
        for i in range(1, len(self.currencies)):
            currency_unit = float(input(
                'Give us the value of 1 ' + self.currencies[i] + ' in ' + self.currencies[0] + '\n>>\t'))
            self.first_col.append(float(format(currency_unit, '.5f')))
            self.first_line.append(self.first_col[0] / float(currency_unit))

    def calculate_matrix(self):
        a = np.array(self.first_col)
        b = np.array(self.first_line)
        self.matrix = np.outer(a, b)

    def show_table(self):
        pd.options.display.float_format = '{:,.5f}'.format
        print(pd.DataFrame(self.matrix, columns=self.currencies, index=self.currencies))


matrix = CurrencyMatrix()
matrix.init()
matrix.calculate_matrix()
matrix.show_table()
