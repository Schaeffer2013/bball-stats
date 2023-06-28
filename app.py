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
    team_total = len(players_data) // len(teams_data)
    experienced_players = [player for player in players_data if player['experience'] == True]
    non_experienced_players = [player for player in players_data if player['experience'] == False]
    

    for team in teams_data:
        balanced_team = {'name': team, 'players':[], 'experienced': 0, 'non_experienced': 0, 'total_height': 0, 'average_height': 0, 'total_players': 0}
        balanced.append(balanced_team)

    for player in players_data:
        if player['experience'] == True and experienced_players:
            balanced_team = balanced.pop(0)
            balanced_team['players'].append(player)
            balanced_team['total_height'] += int(player['height'])
            balanced_team['total_players'] += 1
            balanced.append(balanced_team)
            experienced_players.pop(0)
        elif player['experience'] == False and non_experienced_players:
            balanced_team = balanced.pop(0)
            balanced_team['players'].append(player)
            balanced_team['total_height'] += int(player['height'])
            balanced_team['total_players'] += 1
            balanced.append(balanced_team)
            non_experienced_players.pop(0)

    for balanced_team in balanced:
        balanced_team['players'].sort(key=lambda player: int(player['height']))

    for balanced_team in balanced:
        players_on_team = len(balanced_team['players'])
        if players_on_team > 0:
            balanced_team['average_height'] = round(balanced_team['total_height'] / players_on_team)


    
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
            if choice_picked.lower() != "a" and choice_picked.lower() != "b":
                raise Exception("Sorry invalid choice")
        except ValueError:
            print("Please enter A or B")
            continue
        except Exception as e:
            print(f"{e}")
            continue
        else:
            if choice_picked.lower() == "a" or choice_picked.lower() == "b":
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
                print("Invalid choice, please enter A, B, or C.")
                continue
        except Exception as e:
                print(f"{e}")
                continue
        else:
            if choice_picked.lower() == "a" or choice_picked.lower() == "b" or choice_picked.lower() == "c":
                break
                        
        
       
    team_selected = balanced[ord(choice_picked.lower()) - 97]

    print(f"Team:", {team_selected['name']})
    ("\n-----------------------\n")
    print(f"Total players:", {team_selected['total_players']})


    experienced_players = sum(1 for player in team_selected['players'] if player['experience'] == True)
    non_experienced_players = sum(1 for player in team_selected['players'] if player['experience'] == False)
    print(f"Total experienced: {experienced_players}")
    print(f"Total inexperienced: {non_experienced_players}")
    print(f"Average height: {team_selected['average_height']}")
                print("\nPlayers on Team:")
                for player in team_selected['players']['experienced']:
                    print(player['name'], "(Experienced)")
                for player in team_selected['players']['non_experienced']:
                    print(player['name'], "(Non_Experienced)")
                print("\nGauradians:")
                for player in team_selected['players']['experienced']:
                    print(player['guardians'])
                for player in team_selected['players']['non_experienced']:
                    print(player['guardiands'])
            else:
                print("Team selected not found. Please try again.")


        elif choice_picked.lower() == "b":
            print("Exiting out of the program.")
            break 
        else:
            print("Invalid choice. Please try again.")

    
    
        
             
                


    


if __name__ == "__main__":
    data_collected()
    cleaned = clean_data(players_data)
    balanced = balance_teams(cleaned, teams_data)
    start()
    


    
     
     

            

    




