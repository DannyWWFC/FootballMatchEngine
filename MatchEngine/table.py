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
    def __str__(self):
        sorted_table = sorted(self.values(), key=lambda x: (x.points, x.gd, x.gf), reverse=True)

        print(f"\n{'':2} {'Team':20} {'W':>3} {'D':>3} {'L':>3} {'GF':>4} {'GA':>4} {'GD':>5} {'P':>4}")
        print("-" * 57)
        for i, entry in enumerate(sorted_table, 1):
            print(
                f"{i:2} {entry.team.name:20} "
                f"{entry.wins:3} {entry.draws:3} {entry.losses:3} "
                f"{entry.gf:4} {entry.ga:4} {entry.gd:5} {entry.points:4}"
            )

            if i in(4, 6, 17):
                print("-" * 57)

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