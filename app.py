from constants import PLAYERS, TEAMS
import copy 
players_data = []
teams_data = []
teams = []

def data_collected():
    players_data = copy.deepcopy(PLAYERS)
    teams_data = copy.deepcopy(TEAMS)
    return players_data, teams_data



def clean_data(data):

    for player in data:
        fixed = {}
        fixed ["name"] = player["name"]
        fixed ["guardians"] = player["guardians"].split(" and ")[0]
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(player["height"])
    print(clean_data(data))
    return clean_data(data)
        
    


def level_of_exp(level_exp, leveln_exp):
    players = copy.deepcopy(PLAYERS)

    for player in players:
        if player["experience"] ==  True:
            level_exp.append(player)
        else:
            leveln_exp.append(player)
    
    return players


def balance_teams(level_exp, leveln_exp):
        players = copy.deepcopy(PLAYERS)
        teams = copy.deepcopy(TEAMS)


        panthers = "A"
        bandits = "B"
        warriors = "C"
        players_on_team = level_exp + leveln_exp
        total_team_number = (players_on_team / (teams))
        num_of_players = int(3)
        average_height = round(sum["height"]for players in []) / len(players_on_team)

        for players in panthers:
            if len(level_exp) == num_of_players:
                panthers.append(players["name".join["guardians"]])
            if len(leveln_exp) == num_of_players:
                panthers.append(players["name".join["guardians"]])


        for players in bandits:
             if len(level_exp) == num_of_players:
                bandits.append(players["name".join["guardians"]])
             if len(leveln_exp) == num_of_players:
                  bandits.append(players["name".join["guardians"]])


        for players in warriors:
             if len(level_exp) == num_of_players:
                  warriors.append(players["name".join["guardians"]])
             if len(leveln_exp) == num_of_players:
                  warriors.append(players["name".join["guardians"]])
                
        return balance_teams

























def start():
    players = copy.deepcopy(PLAYERS)
    teams = copy.deepcopy(TEAMS)


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
    ("\n-----------------------\n")
    print("Total players:    ")
    print("Total experienced:    ")
    print("Total inexperienced:    ")
    print("Average height:    ")

    ("\n")
    print("Players on Team:")

    ("\n")
    print("Guardians:")
    
        
             
                


    


if __name__ == "__main__":
    print(clean_data(clean_data))
     
     

            

    




