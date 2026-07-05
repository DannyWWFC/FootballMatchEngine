import numpy as np
from team import Team
from result import MatchResult

MIN_XG = 0.5
GOAL_SCALE = 3.0

class MatchEngine:
    def __init__(self, base_goals: float = 1.35, home_advantage: float = 0.25, strength_power: float = 1.2):
        self.base_goals = base_goals
        self.home_advantage = home_advantage
        self.strength_power = strength_power

    def _expected_goals(self, attack_strength: float, defence_strength: float):
        return self.base_goals * (attack_strength / defence_strength) ** self.strength_power

    def simulate_match(self, home_team: Team, away_team: Team):
        # Strength smoothing (prevents extreme ratios dominating)
        home_attack = home_team.strength ** self.strength_power
        away_attack = away_team.strength ** self.strength_power

        total = home_attack + away_attack

        # Expected goals with home advantage
        home_xg = self.base_goals * (home_attack / total) * 2 + self.home_advantage
        away_xg = self.base_goals * (away_attack / total) * 2

        # Safety bounds (prevents unrealistic explosions)
        home_xg = max(0.1, min(home_xg, 4.5))
        away_xg = max(0.1, min(away_xg, 4.5))

        home_goals = np.random.poisson(home_xg)
        away_goals = np.random.poisson(away_xg)

        return MatchResult(home_team, away_team, home_goals, away_goals)