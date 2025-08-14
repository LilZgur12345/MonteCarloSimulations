# Problem 1
import random

def roll(num_dice):
  dice_faces = []
  for i in range(num_dice):
    # Add random dice faces to the list
     output = random.randint(1,6)
     dice_faces.append(output)
  return dice_faces

def monte_carlo():
  count1 = 0
  count2 = 0
  num_trials = 100000
  for j in range(num_trials):
    # Roll 5 dice
    roll_the_dice = roll(5)
    sum_of_dice = sum(roll_the_dice)
    if sum_of_dice == 16:
      count1 = count1 + 1
    if sum_of_dice == 20:
      count2 = count2 + 1
  probability1 = (count1 / num_trials)
  print('Probability that the sum of the faces equals 16: ' + str(probability1))
  probability2 = (count2 / num_trials)
  print('Probability that the sum of the faces equals 20: ' + str(probability2))
  return probability1 > probability2
