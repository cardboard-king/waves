def start_data_function(mode, parameters):
    values = {
        'zeros'         : np.zeros(parameters[0]), 
        'gaussian' : gaussian(parameters[3], parameters[4], parameters[1], parameters[2], parameters[0])
    }[mode]
    return values
