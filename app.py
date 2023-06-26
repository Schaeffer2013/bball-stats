from constants import PLAYERS, TEAMS
import copy 
players_data = []
teams_data = []
team = []

def data_collected():
    global players_data
    global teams_data
    global team
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
    balanced = []
        #average_height = total_height / players_on_team
    team_total = len(players_data) // len(teams_data)


    for team_name in teams_data: 
            organize_team = {
                'team': team_name,
                'players': []
            }
            
            balanced.append(organize_team)
            
            num_exp = []
            num_non_exp = []

            for player in players_data:
                if player['experience'] == 'YES':
                   num_exp.append(player)
                else:
                     num_non_exp.append(player)
              
             
                 
    
            
            organize_team['players'].append(player)
            print(organize_team)
                    
                   
                   #if len(team_players) == team_total:
                    #break
            

    return balanced









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
    print(f"Team:   {team['name']}   ")
    ("\n-----------------------\n")
    print(f"Total players:   {team}")
    print(f"Total experienced:   {team['experienced']}    ")
    print(f"Total inexperienced:   {team['non_experienced']}    ")
    print(f"Average height:   {average_height}    ")

    ("\n")
    print("Players on Team:")

    ("\n")
    print("Guardians:")
    
        
             
                


    


if __name__ == "__main__":
    data_collected()
    cleaned = clean_data(players_data)
    balanced = balance_teams(cleaned, teams_data)


    
     
     

            

    




