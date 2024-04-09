import sys
sys.path.append('..')

from src.dater import DataGenerator
from src.modeller import ModelGenerator
from src.plotter import PlotterGenerator

dater = DataGenerator()
dater.load_well()
dater.select_data()
dater.plot_me(legend='Original')

dater.add_noise(level=0.3)
dater.plot_me(legend='With noise')

model = ModelGenerator(data=dater.get_data())

model.k_means(n_clusters=16)
model.gmm(n_clusters=16)

plotter = PlotterGenerator()
for hue in ['KMEANS', 'GMM']:
    plotter.crossplots(dataset=dater.get_data(), hue=hue)

