import random
from team import Team

# Simulate matches
def simulate_match(team1, team2):
    total = team1.strength + team2.strength
    winner = random.random()

    if winner < team1.strength / total:
        return team1
    return team2

team1 = Team("Wolves", 5)
team2 = Team("Man City", 20)

team1wins = 0
team2wins = 0
for i in range(0, 100):
    winner = simulate_match(team1, team2)
    if winner is team1:
        team1wins += 1
    else:
        team2wins += 1

print(f"{team1.name} wins: {team1wins}")
print(f"{team2.name} wins: {team2wins}")
