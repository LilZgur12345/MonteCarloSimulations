# Problem 3
import random
def monte_carlo(n):
    NY_ATL = 866
    NY_NSH = 900
    NY_ATL_NOLA_Dallas = 975
    NY_ATL_STLouis_Dallas = 1217
    NY_NSH_NOLA_Dallas = 1037
    NY_NSH_STLouis_Dallas = 971

    Nashville_Distance = []
    Atlanta_Distance = []
    route1 = [NY_ATL, NY_NSH]
    route2 = [NY_ATL_NOLA_Dallas, NY_ATL_STLouis_Dallas]
    route3 = [NY_NSH_STLouis_Dallas, NY_NSH_NOLA_Dallas]
    route4 = [NY_ATL_STLouis_Dallas, NY_ATL_NOLA_Dallas, NY_NSH_STLouis_Dallas, NY_NSH_NOLA_Dallas]

    for i in range(n):
      mad_max = 0
      wicked_witch = random.randint(0,1)
      MM_loc1 = random.randint(0,1) # First index
      mad_max = mad_max + route1[MM_loc1]
      if route1[MM_loc1] == NY_ATL:
          start_from = "Atlanta"
          next_route = route2
      else:
          start_from = "Nashville"
          next_route = route3

      MM_loc2 = random.randint(0,1) # Second index
      current_route = next_route[MM_loc2]

      if next_route[MM_loc2] == next_route[wicked_witch]:
        # Run into Wicked Witch
        if MM_loc2 == 0:
          mad_max = mad_max + next_route[MM_loc2 + 1]
          # Switch routes
        else:
          mad_max = mad_max + next_route[MM_loc2 - 1]
          # Switch routes
      else:
        mad_max = mad_max + next_route[MM_loc2]
        # Correct route
      if start_from == "Atlanta":
        Atlanta_Distance.append(mad_max)
      else:
        Nashville_Distance.append(mad_max)

    ATL_Total = sum(Atlanta_Distance) / len(Atlanta_Distance)
    NSH_Total = sum(Nashville_Distance) / len(Nashville_Distance)

    if ATL_Total < NSH_Total:
      print('Starting from Atlanta is the shorter route')
    else:
      print('Starting from Nashville is the shorter route')
    return 'Atlanta Miles: ' + str(ATL_Total), 'Nashville Miles: ' + str(NSH_Total)

result = monte_carlo(n = 100000)
result