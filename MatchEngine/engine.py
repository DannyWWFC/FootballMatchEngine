import numpy as np
from team import Team
from result import MatchResult

MIN_XG = 0.5
GOAL_SCALE = 3.0

class MatchEngine:
    def simulate_match(self, home_team: Team, away_team: Team):
        total = home_team.strength + away_team.strength

        home_xg = 0.8 + 2.5 * (home_team.strength / total)
        away_xg = 0.8 + 2.5 * (away_team.strength / total)

        home_goals = np.random.poisson(home_xg)
        away_goals = np.random.poisson(away_xg)

        return MatchResult(home_team, away_team, home_goals, away_goals)