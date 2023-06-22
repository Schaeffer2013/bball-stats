from constants import PLAYERS, TEAMS
import copy 
players_data = []
teams_data = []
teams = []

def data_collected():
    global players_data
    global teams_data
    players_data = copy.deepcopy(PLAYERS)
    teams_data = copy.deepcopy(TEAMS)



def clean_data(players_data):
    cleaned = []

    for player in players_data:
        fixed = {}
        fixed ['name'] = player['name']
        fixed ['guardians'] = player['guardians'].split( 'and' )
        if player['experience'] == "YES":
           fixed['experience'] = True
        else:
            player['experience'] == "NO"
            fixed['experience'] = False
        height_str = player['height']
        height_str = height_str.replace(' inches', '')
        height_int = int(height_str)
        fixed ['height'] = height_int
        

        cleaned.append(fixed)
    return cleaned




def balance_teams(players_data, teams_data):

        exp = ['experience', True]
        n_exp = ['experience', False]
        panthers = 'A'
        bandits = 'B'
        warriors = 'C'
        players_on_team = exp + n_exp
        total_team_number = len(players_data) / len(teams_data)
        num_of_players = int(3)
        

        total_height = 0
        for player in players_data:
             height =  
             total_height += height

        for players in players_data, teams_data:
            if len(exp) == num_of_players:
                panthers.append(players['name'.join['guardians']])
                print(panthers['name'.join['guardians']])
            if len(n_exp) == num_of_players:
                panthers.append(players['name'.join['guardians']])


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
    data_collected()
    cleaned = clean_data(players_data)
    balance_teams(players_data, teams_data)
    
     
     

            

    




