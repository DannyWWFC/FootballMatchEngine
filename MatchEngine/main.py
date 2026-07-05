import random
from team import Team
from engine import MatchEngine

engine = MatchEngine()

home_team = Team("Wolves", 5)
away_team = Team("Man City", 20)

for i in range(0, 10):
    results = []

    for i in range(0, 1000):
        result = engine.simulate_match(home_team, away_team)
        results.append(result)

    total_home_goals = 0
    total_away_goals = 0

    highest_home_win = None
    highest_home_margin = -1

    highest_away_win = None
    highest_away_margin = -1

    for r in results:
        total_home_goals += r.home_goals
        total_away_goals += r.away_goals

        # Home win
        margin = r.home_goals - r.away_goals
        if margin > highest_home_margin:
            highest_home_margin = margin
            highest_home_win = r

        # Away win
        away_margin = r.away_goals - r.home_goals
        if away_margin > highest_away_margin:
            highest_away_margin = away_margin
            highest_away_win = r

    avg_home_goals = total_home_goals / len(results)
    avg_away_goals = total_away_goals / len(results)

    print("=== STATS ===\n")

    print(f"Average home goals: {avg_home_goals:.2f}")
    print(f"Average away goals: {avg_away_goals:.2f}\n")

    print("Biggest home win:")
    print(highest_home_win)

    print("\nBiggest away win:")
    print(f"{highest_away_win}\n")