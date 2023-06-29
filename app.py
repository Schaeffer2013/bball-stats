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
    balanced_teams = []
    team_total = len(players_data) // len(teams_data)
    experienced_players = [player for player in players_data if player['experience'] == True]
    non_experienced_players = [player for player in players_data if player['experience'] == False]
    num_teams = len(teams_data)
    num_exp_players = len(experienced_players)
    num_non_exp_players = len(non_experienced_players)
    total_exp_per_team = num_exp_players // num_teams
    total_non_exp_per_team = num_non_exp_players // num_teams

    for team in teams_data:
        balanced_team = {'name': team, 'players': [], 'experienced': 0, 'non_experienced': 0, 'total_height': 0, 'average_height': 0, 'total_players': 0, 'guardians': []}
        balanced_teams.append(balanced_team)


    team_index = 0
    while experienced_players:
        player = experienced_players.pop(0)
        team = balanced_teams[team_index]
        team['players'].append(player)
        team['guardians'].append(player['guardians'])
        team['total_height'] += int(player['height'])
        team['total_players'] += 1
        team_index = (team_index + 1) % num_teams

    team_index = 0
    while non_experienced_players:
        player = non_experienced_players.pop(0)
        team = balanced_teams[team_index]
        team['players'].append(player)
        team['guardians'].append(player['guardians'])
        team['total_height'] += int(player['height'])
        team['total_players'] += 1
        team_index = (team_index + 1) % num_teams


    for balanced_team in balanced_teams:
        balanced_team['players'].sort(key=lambda player: int(player['height']))

    for balanced_team in balanced_teams:
        players_on_team = len(balanced_team['players'])
        if players_on_team > 0:
            balanced_team['average_height'] = round(balanced_team['total_height'] / players_on_team, 1)


    
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
            if choice_picked.lower() != "a" and choice_picked.lower() != "b":
                raise Exception("Sorry invalid choice")
        except ValueError:
            print("Please enter A or B")
            continue
        except Exception as e:
            print(f"{e}")
            continue

        if choice_picked.lower() == "a":
              display_team_stats()
              break
        elif choice_picked.lower() == "b":
                  print("Maybe next time, bye for now.")
                  break

def display_team_stats():

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
                print("Invalid choice, please enter A, B, or C.")
                continue
            except Exception as e:
                print(f"{e}")
                continue
            else:
                if choice_picked.lower() == "a" or choice_picked.lower() == "b" or choice_picked.lower() == "c":
                   break
                        
        
       
        team_selected = balanced_teams[ord(choice_picked) - 97]

        print("Team:", team_selected['name'])
        ("\n-----------------------\n")

        print("Total players:", len(team_selected['players']))
        print("Total experienced:", len([player for player in team_selected['players'] if player['experience'] == True]))
        print("Total inexperienced:", len([player for player in team_selected['players'] if player['experience'] == False]))
        print("Average height:", (team_selected['average_height']))
        print("\nPlayers on Team:")
        players_list = ", " .join([player['name']for player in team_selected['players']])
        print(f"{players_list}")
        print("\nGuardians on Team:")
        guardians_list = ", " .join([guardian.strip() for guardians in team_selected['guardians'] for guardian in guardians])
        print(f"{guardians_list}")
        more_stats()

def more_stats():
    while True:
        proceed = input("\n""Would you like to see more team statistics?  (Y/N)   ")
        if proceed.lower() == 'y' :
            start()
        elif proceed.lower() == 'n' :
            print("Thank you for viewing the statistics!")
            break
        else:
            print("Sorry that was a invalid choice, please enter a Y or N")





    
    
        
             
                


    


if __name__ == "__main__":
    data_collected()
    cleaned = clean_data(players_data)
    balanced_teams = balance_teams(cleaned, teams_data)
    start()
    
    


    
     
     

            

    




