from team import Team

class TeamRepository:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.teams = []
        return cls._instance

    def add_team(self, team: Team):
        self.teams.append(team)

    def get_team(self, name: str):
        for team in self.teams:
            if team.name == name:
                return team
        return None

    def get_all_teams(self):
        return self.teams

    def clear(self):
        self.teams.clear()