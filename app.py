from constants import PLAYERS, TEAMS
import copy 
players_data = []
teams_data = []
teams = []

def data_collected():
    global players_data
    global teams_data
    global teams
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


        exp = []
        n_exp = []
        players_on_team = []
        total_team_number = len(players_data) / len(teams_data)
        num_teams = len(teams_data)
        team = []
        

        total_height = 0
        for team, players_on_team
        for player in players_data:
             height = player['height']
             total_height += height
        

        for player in players_data:
            if player['experience'] == 'YES':
                 exp.append(player)
            else:
                 n_exp.append(player)
    
        for index in range(num_teams):
             team = teams_data[index]
             players_on_team.extend(exp[index::num_teams])
             players_on_team.extend(n_exp[index::num_teams])

        for index, player in enumerate(players_data, 1):
             team = teams_data[(index - 1) % num_teams]
             player['team'] = team

                
        return balance_teams
def print_players(players)








def start():
    players_data = copy.deepcopy(PLAYERS)
    teams_data = copy.deepcopy(TEAMS)


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
    balance_teams(cleaned, teams_data)
    start()
    
     
     

            

    




