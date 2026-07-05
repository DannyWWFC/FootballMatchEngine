import random
from collections import defaultdict
from team import Team
from engine import MatchEngine
from table import Table

engine = MatchEngine()

teams = [
    Team("AFC Bournemouth", 10),
    Team("Arsenal", 18),
    Team("Aston Villa", 14),
    Team("Brentford", 11),
    Team("Brighton", 10),
    Team("Chelsea", 16),
    Team("Coventry", 7),
    Team("Crystal Palace", 9),
    Team("Everton", 11),
    Team("Fulham", 11),
    Team("Hull", 5),
    Team("Ipswich", 6),
    Team("Leeds", 8),
    Team("Liverpool", 17),
    Team("Man City", 19),
    Team("Man United", 16),
    Team("Newcastle", 12),
    Team("Nottm. Forest", 8),
    Team("Sunderland", 10),
    Team("Tottenham", 12)]

tables = []
title_wins = defaultdict(int)

for i in range (0, 10):
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

