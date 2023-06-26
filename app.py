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


        experienced = []
        non_experienced = []
        players_on_team = []
        num_teams = len(teams_data)
        team = []
        team_exp_count = {team:  {'experienced': 0, 'non_experienced': 0} for team in teams_data}
        
             
                  
        for player in players_data:
           total_per_team = len(players_data) / len(teams_data)
           team = min(team_exp_count, key=lambda x: team_exp_count[x]['experienced'] + team_exp_count[x]['non_experienced'])

           if player['experience'] == 'YES':
                 team_exp_count[team]['experienced'] += 1
           else:
                 team_exp_count[team]['non_experienced'] +=1
           player['team'] = team


        for team_name in teams_data:
             team = {'name': team_name, 'Total players': 6, 'Experienced players': 3, 'Non-experienced players': 3, 'Average height': 0, 'players':[], 'Guardians': []}
             teams.append(team)

        

        for index, player in enumerate(players_data, 1):
             team = teams_data[(index - 1) % num_teams]
             player['team'] = team

     
        for players in players_data:
             total_height = 0
             players_on_team = len(players)    
             
             for player in players:
                  height = height_int
                  total_height += height

             if players_on_team > 0:
                  average_height = total_height / players_on_team
             else:
                  average_height = 0
             
        
        return balance_teams









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

    
     
     

            

    




