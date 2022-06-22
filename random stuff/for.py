# list = [1, 6, 9, 10, 6, 2]

# print(f"{list = }")

# print(f"{len(list) = }")

# for i in range(len(list)):
#     print(f"{i = }")

# for item in list:
#     print(f"{item = }")

from random import *
player = []

for i in range(20):
  # code to randomly assign a team and player to each player
  team = randint(1,2)
  score = randint(5, 50)
  player.append([team, score])

print(f"{player = }")

team1Count = 0
team2Count = 0

for i in range(len(player)):
    # print(f"{player[i] = }")
    thisPlayer = player[i]
    # print(f"{thisPlayer = }")
    if thisPlayer[0] == 1:
        # print("its a one")
        team1Count = team1Count + thisPlayer[1]
    else:
        team2Count = team2Count + thisPlayer[1]

print("Team 1 score:", team1Count)
print("Team 2 score:", team2Count)
