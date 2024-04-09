import sys
sys.path.append('..')

from src.dater import DataGenerator
from src.modeller import ModelGenerator

dater = DataGenerator()
dater.load_well()
dater.select_data()
dater.plot_me(legend='Original')

model = ModelGenerator(data=dater.get_data())
model.optimise_k_means(max_k=16)
