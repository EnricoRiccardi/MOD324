import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

   
class DataGenerator:
    def __init__(self, description='Data generator'):
        """Initializes the class creating the required attributes."""
        self.description = description    
        self.df = None 

    def load_well(self, data_file="../Teaching/MOD323/src/data/xeek_train_subset_mini.csv", well_name="16/10-1"):
        """Read a dataset.""" 
        self.df = pd.read_csv(data_file)
        self.df = self.df[self.df["WELL"] == well_name] # select data only for the specific well

    def remove_nan(self):
        self.df.dropna(inplace=True)
    
    def add_noise(self, properties=["RHOB", "GR"], level=0.1):
        """Adds noise to the data."""
        # Noise for GR is different than that for RHOB due to the usual values of those two measurements. RHOB usually varies between 1.9-2.9 g/cm3 wheres GR between 5-300.
        for property in properties:
            if property == "RHOB":
                range = [-level, level]
            if property == "GR":
                range = [-level*50, level*50]

            noise = np.random.uniform(low=range[0], high=range[1], size=len(self.df[property]))
            self.df[property] += noise
    
    def plot_me(self, x_lab='RHOB', y_lab='GR', legend=''):
        """Plots datasets."""
        plt.scatter(self.df[x_lab], self.df[y_lab], label=legend)
        plt.xlabel(x_lab)
        plt.ylabel(y_lab)
        plt.legend()

    def get_data(self):
        return self.df
