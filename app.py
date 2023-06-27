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


import random

def balance_teams(players_data, teams_data):
    balanced_teams = []
    team_total = len(players_data) // len(teams_data)

    for team in teams_data:
        balanced_team = {'name': team, 'players': {'experienced':[], 'non_experienced': []}, 'players_height': 0, 'average_height': 0}
        balanced_teams.append(balanced_team)
        experienced_players = [player for player in players_data if player['experience'] == True]
        non_experienced_players = [player for player in players_data if player['experience'] == False]

        random.shuffle(experienced_players)
        random.shuffle(non_experienced_players)

    for team in balanced_teams:
        while len(team['players']['experienced']) < len(experienced_players) // len(teams_data):
             if experienced_players:
                  player = experienced_players.pop()
                  team['players']['experienced'].append(player)
                  #team['players_height'] += int(player['height'].split()[0])


    for team in balanced_teams:
        while len(team['players']['non_experienced']) < len(non_experienced_players) // len(teams_data):
             if non_experienced_players:
                  player = non_experienced_players.pop()
                  team['players']['non_experienced'].append(player)
                  #team['players_height'] += int(player['height'].split()[0])
    #for team in balanced_teams:
         #team['players']['experienced'].sort(key=lambda player)
    for team in balanced_teams:
         players_on_team = len(team['players']['experienced']) + len(team['players']['non_experienced'])
         if players_on_team > 0:
              team['average_height'] = team['players_height'] / players_on_team
    #print(balanced_teams)
    #for player in players_data:
         




    print(balanced_teams)
    return balanced_teams









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
    print(f"Average height:    ")

    ("\n")
    print("Players on Team:")

    ("\n")
    print("Guardians:")
    
        
             
                


    


if __name__ == "__main__":
    data_collected()
    cleaned = clean_data(players_data)
    balanced_teams = balance_teams(cleaned, teams_data)


    
     
     

            

    




