from team import Team

class MatchResult:
    def __init__(self, home_team: Team, away_team: Team, home_goals: int, away_goals: int):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = home_goals
        self.away_goals = away_goals

    @property
    def winner(self):
        if self.home_goals > self.away_goals:
            return self.home_team
        elif self.away_goals > self.home_goals:
            return self.away_team
        return None

    @property
    def is_draw(self):
        return self.home_goals == self.away_goals

    def __str__(self):
        return (f"{self.home_team.name} {self.home_goals} - "
                 f"{self.away_goals} {self.away_team.name}")