# Problem 2
import random

#1/5 Truth
friend1 = ['TRUTH', 'LIE', 'LIE', 'LIE', 'LIE']
friend2 = ['TRUTH', 'LIE', 'LIE', 'LIE', 'LIE']
#1/3 Truth
friend3 = ['TRUTH', 'TRUTH', 'LIE']
friend4 = ['TRUTH', 'TRUTH', 'LIE']

def monte_carlo_truth(n):
  responses = []
  for i in range(n):
    # Shuffle the probabilities
      random.shuffle(friend1), 
      random.shuffle(friend2), 
      random.shuffle(friend3), 
      random.shuffle(friend4)

      # Add to the list
      responses.append(
          (friend1[0]=='TRUTH') and
          (friend2[0]=='TRUTH') and
          (friend3[0]=='TRUTH') and
          (friend4[0]=='TRUTH')
      )

# P(not A) = not all of the friends are telling the truth
  result = 1 - (sum(responses) / n)
  return result