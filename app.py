from constants import PLAYERS, TEAMS
import copy 
players = PLAYERS.copy()
teams = TEAMS.copy()
import constants
TEAMS = []
PLAYERS = {}


def clean ():
    global TEAMS
    global PLAYERS
    cleaned = []
    for players in PLAYERS:
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


def level_of_exp():
    global TEAMS
    global PLAYERS

    level_exp = []
    leveln_exp = []

    for player in players:
        if player["experience"] ==  True:
            level_exp.append(player)
        else:
            leveln_exp.append(player)
        return players


def balance_teams():
        global TEAMS
        global PLAYERS

        level_exp = []
        leveln_exp = []


        panthers = []
        bandits = []
        warriors = []
        players_on_team = level_exp + leveln_exp
        total_team_number = len(players_on_team / len(teams))
        num_of_players = int(3)
        average_height = round(sum["height"]for players in []) / len(players_on_team)

        for players in panthers:
            if len(level_exp) == num_of_players:
                panthers.append(players["name".join["guardians"]])
            if len(leveln_exp) == num_of_players:
                panthers.append(players["name".join["guardians"]])


        for players in bandits:
             if len(level_exp) == num_of_players:
                bandits.append(players["name"])
             if len(leveln_exp) == num_of_players:
                  bandits.append(players["name"])


        for players in warriors:
             if len(level_exp) == num_of_players:
                  warriors.append(players["name"])
             if len(leveln_exp) == num_of_players:
                  warriors.append(players["name"])
        print(balance_teams)
        return balance_teams

























def start():
    global TEAMS
    global PLAYERS


    print("Welcome to the Basketball Team Stats tool")
    print("\n-----MENU-----\n")

    print("Please choose option A or B:   ")
    print("A. Display Team Stats")
    print("B. Quit")
    ("\n")
    while True:
        try:
                choice_picked = input(" ")
                if choice_picked != "a" and choice_picked != "b":
                   raise Exception("Sorry invalid choice")
        except ValueError:
                print("Please enter A or B")
                continue
        except Exception as e:
                print(f"{e}")
                continue
        else:
             choice_picked.lower() == "a" or choice_picked.lower() == "b"
             break 

    print("Choose a team by entering the corresponding letter.")
    print("A. Panthers")
    print("B. Bandits")
    print("C. Warriors")
    ("\n")
    while True:
        try: 
                choice_picked = input(" ")
                if choice_picked != "a" and choice_picked != "b" and choice_picked != "c":
                    raise Exception("Sorry invalid choice")
        except ValueError:
                print("Please enter A, B, or C")
                continue
        except Exception as e:
                print(f"{e}")
                continue
        else:
             choice_picked.lower() == "a" or choice_picked.lower() == "b" or choice_picked.lower() == "c"
             break
    print("Team:      ")
    ("\n")
    
        
             
                


    


if __name__ == "__main__":
     balance_teams()
     

            

    




