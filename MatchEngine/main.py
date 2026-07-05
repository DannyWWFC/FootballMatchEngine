import random
import json
from collections import defaultdict
from team import Team
from engine import MatchEngine
from table import Table

engine = MatchEngine()

with open("leagues/championship.json", "r") as f:
    team_data = json.load(f)

teams = [
    Team(item["name"], item["strength"])
    for item in team_data
]

tables = []
title_wins = defaultdict(int)

for i in range (0, 100):
    table, results = engine.simulate_season(teams)
    tables.append(table)

    winner = max(table.values(), key=lambda entry: entry.points)
    title_wins[winner.team.name] += 1

highest_points = 0

for i, table in enumerate(tables, 1):
    winner = max(table.values(), key=lambda entry: entry.points)

    if winner.points > highest_points:
        highest_points = winner.points

    year = 2026 + i

    print(f"Season {year}/{year+1}: Winner = {winner.team.name} ({winner.points} pts)")


print("\n=== TITLE COUNTS ===")

for team, wins in sorted(title_wins.items(), key=lambda x: x[1], reverse=True):
    print(f"{team}: {wins} titles")

print(f"\nHighest points tally in a season: {highest_points}");

