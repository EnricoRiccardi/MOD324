import os
import sys
sys.path.append('..')

import unittest
from src.dater import DataGenerator


class MyDataTest(unittest.TestCase):
    def test_datar_init(self):
        dataclass = DataGenerator()
        self.assertTrue(type(dataclass), 'class')  # add assertion here

    def test_datar_load_well(self):
        dataclass = DataGenerator()
        path = os.path.abspath('.')
        dataclass.load_well(data_file=os.path.join(path, 'xeek_train_subset_mini.csv'))
        print(dataclass.df['DEPTH_MD'].iloc[1])
        self.assertTrue(dataclass.df['DEPTH_MD'].iloc[1] == 439.56778984)


if __name__ == '__main__':
    unittest.main()
