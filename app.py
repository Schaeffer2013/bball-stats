from constants import PLAYERS, TEAMS
import copy 
players = PLAYERS.copy()
teams = TEAMS.copy()
import constants
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


def balance_teams():
        global TEAMS
        global PLAYERS

        level_exp = []
        leveln_exp = []


        panthers = []
        bandits = []
        warriors = []
        players_on_team = level_exp + leveln_exp
        num_of_players = int(3)
        average_height = round(sum["height"]for players in []) / len(players_on_team)

        for players in panthers:
            if len(level_exp) == num_of_players:
                panthers.append(players["name"])
            if len(leveln_exp) == num_of_players:
                panthers.append(players["name"])


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

























def start():
    global TEAMS
    global PLAYERS


    print("Welcome to the Basketball Team Stats tool")
    print("\n-----MENU-----\n")

    input("Please choose option A or B:   ")
    print("A. Display Team Stats")
    print("B. Quit")
    while True:
        try:
                choice_picked = input(" ")
                if choice_picked != ("A or B"):
                   raise Exception("Sorry invalid choice")
        except ValueError:
                print("Please enter A or B")
                continue
        except Exception as e:
                print(f"{e}")
                continue
        input("Choose a team by entering the corresponding letter.")
        print("A. Panthers")
        print("B. Bandits")
        print("C. Warriors")

    
            choice_picked = input(" "):
            if choice_picked != ("A, B, or C"):
                raise Exception("Sorry invalid choice")
        except ValueError:
                print("Please enter A, B, or C")
        
                
                break
        elif choice_picked != ("A, B, or C"):
                print("Sorry invalid choice")
                print("Please enter A, B, or C")
                continue
        else:
             choice_picked.lower() == "b"
             print("Maybe next time.")
             break
    
        
             
                


    


if __name__ == "__main__":
     start()
            

    




