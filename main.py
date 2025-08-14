from src.problem1 import monte_carlo
from src.problem2 import monte_carlo_truth
from src.problem3 import monte_carlo_route
from src.problem4 import monte_carlo_normal

def main():
    # Problem 1
    result1 = monte_carlo()
    print('The first probability is greater than the second: ' + str(result1))

    # Problem 2
    n = 100000
    result2 = monte_carlo_truth(n)
    print('Probability that NOT all friends are telling the truth: ' + str(result2))

    # Problem 3
    result3 = monte_carlo_route(n)
    print(result3[0])
    print(result3[1])

    # Problem 4
    result4 = monte_carlo_normal(n)
    print('Final estimated probability is: ' + str(result4))

if __name__ == "__main__":
    main()