well_data = Data_generator()
well_data.load_well()
well_data.plot_me(legend='Original')

well_data.add_noise(level=0.3)
well_data.plot_me(legend='With noise')

# Find out what is the optimal number of clusters
well_model = Model_generator(data=well_data.get_data())
well_model.optimise_k_means(max_k=16)