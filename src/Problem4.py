# Problem 4

from scipy.stats import norm
import matplotlib.pyplot as plt

def monte_carlo_normal(n=100000, show_plot=True):
    population = norm.rvs(size=n, loc=4, scale = 3)
    X = (population > -1) & (population < 2)
    count = sum((X==True))
    probability = count / n
    print('The probability is: ' + str(probability))

    if show_plot:
        plt.hist(population, bins = 20, edgecolor = 'black')
        plt.title('Histogram of Normal Distribution (mean=4, std=3)')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()
    return probability