def gaussian( mu, sig, start, stop, datapoints):
    x = np.linspace(start, stop, datapoints)
    return np.exp(-np.power(x - mu,  2.)/(2*np.power(sig, 2.)))
