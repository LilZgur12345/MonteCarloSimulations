# Problem 4
from scipy.stats import norm
import matplotlib.pyplot as plt
n=100000
population = norm.rvs(size=n, loc=4, scale = 3)
population
X = ((population>-1) & (population<2))
count = sum((X==True))
print('The probability is: ' + str(count/n))
plt.hist(population, bins = 20)
plt.show()