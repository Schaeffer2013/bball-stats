import copy 
import constants
from constants import PLAYERS, TEAMS
TEAMS = []
PLAYERS = {}

def clean_players():
    global TEAMS
    global PLAYERS

    cleaned = []
    for players in constants:
        fixed = {}
        fixed ["name"] = players["name"]
        fixed ["guardians"] = players["guardians"].split(" and ")[0]
        if players["experience"] == "True":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(players["height"])
        cleaned.append(fixed)
    return cleaned



# Sarah is awesome
    def balance_teams():