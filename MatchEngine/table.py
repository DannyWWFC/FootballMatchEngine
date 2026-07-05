class TableEntry:
    def __init__(self, team):
        self.team = team
        self.points = 0
        self.gf = 0
        self.ga = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0

    @property
    def gd(self):
        return self.gf - self.ga

class Table:
    @staticmethod
    def print_table(table):
        sorted_table = sorted(table.values(), key=lambda x: (x.points, x.gd, x.gf), reverse=True)

        print("\n=== LEAGUE TABLE ===\n")

        for i, entry in enumerate(sorted_table, 1):
            print(
                f"{i}. {entry.team.name:20}"
                f"W:{entry.wins} "
                f"D:{entry.draws} "
                f"L:{entry.losses} "
                f"GF:{entry.gf} "
                f"GA:{entry.ga} "
                f"GD:{entry.gd}"
                f"  P:{entry.points} "
            )

    @staticmethod
    def update_table(table, result):
        home = table[result.home_team.name]
        away = table[result.away_team.name]

        home.gf += result.home_goals
        home.ga += result.away_goals

        away.gf += result.away_goals
        away.ga += result.home_goals

        if result.home_goals > result.away_goals:
            home.points += 3
            home.wins += 1
            away.losses += 1

        elif result.home_goals < result.away_goals:
            away.points += 3
            away.wins += 1
            home.losses += 1

        else:
            home.points += 1
            away.points += 1
            home.draws += 1
            away.draws += 1