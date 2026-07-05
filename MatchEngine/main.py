import random
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
    Team("Fulham", 12),
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

table, results = engine.simulate_season(teams)

Table.print_table(table)

