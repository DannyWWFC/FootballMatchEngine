import requests

from team import Team
from player import Player
from team_repository import TeamRepository


def load_fpl_data():
    response = requests.get(
        "https://fantasy.premierleague.com/api/bootstrap-static/"
    )
    response.raise_for_status()

    data = response.json()

    positions = {
        p["id"]: p["singular_name"]
        for p in data["element_types"]
    }

    repository = TeamRepository()
    repository.clear()

    # Temporary lookup from FPL team ID -> Team object
    team_lookup = {}

    # Create Team objects
    for team_data in data["teams"]:
        team = Team(team_data["name"])
        repository.add_team(team)
        team_lookup[team_data["id"]] = team

    # Create Player objects and add them to their Team
    for player_data in data["elements"]:
        player = Player(
            first_name=player_data["first_name"],
            last_name=player_data["second_name"],
            position=positions[player_data["element_type"]],
            price=player_data["now_cost"] / 10,
            total_points=player_data["total_points"],
            minutes=player_data["minutes"]
        )

        team_lookup[player_data["team"]].add_player(player)

    for t in repository.get_all_teams():
        # Sort players by total FPL points (highest first)
        top_players = sorted(
            t.players,
            key=lambda p: p.total_points,
            reverse=True
        )[:15]

        points_per_90 = []

        for player in top_players:
            if player.minutes > 0:
                p90 = player.total_points / (player.minutes / 90)
                points_per_90.append(p90)

        if points_per_90:
            average = sum(points_per_90) / len(points_per_90)
        else:
            average = 0

        t.set_strength(average)


    return repository


if __name__ == "__main__":
    repository = load_fpl_data()

    for team in repository.get_all_teams():
        print(f"{team.name} ({len(team.players)} players)")

        for player in team.players:
            print(f"  - {player}")

        print()