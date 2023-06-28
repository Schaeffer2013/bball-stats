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
        balanced_team = {'name': team, 'players':[], 'exerienced': 0, 'non_experienced': 0, 'average_height': 0}
        balanced.append(balanced_team)

    for player in players_data:
        if player['experience'] == True and experienced_players:
            balanced_team = balanced.pop(0)
            balanced_team['players'].append(player)
            balanced_team['total_height'] += int(player['height'])
            balanced.append(balanced_team)
            experienced_players.pop(0)
        elif player['experience'] == False and non_experienced_players:
            balanced_team = balanced.pop(0)
            balanced_team['players'].append(player)
            balanced_team['total_height'] += int(player['height'])
            balanced.append(balanced_team)
            non_experienced_players.pop(0)

    for balanced_team in balanced:
        players_on_team = len(balanced_team['players'])
        if players_on_team > 0:
            balanced_team['average_height'] = balanced_team['total_height'] / players_on_team


    
    
    print(balanced)
    return balanced

 
         
    

    #for team in balanced_teams:

       
       
       
       
               
    #for team in balanced_teams:
     # team['players']['experienced'].sort(key=lambda player: int(player['height']))
      #   team['players']['non_experienced'].sort(key=lambda player: int(player['height']))
    #for team in balanced_teams:
     #    players_on_team = len(team['players']['experienced']) + len(team['players']['non_experienced'])
      #   if players_on_team > 0:
       #       team['average_height'] = team['players_height'] / players_on_team
   
    
  









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
        choice_picked = input(" ")
        if choice_picked.lower() == "a":
            print("Choose a team by entering the corresponding letter.")
            print("A. Panthers")
            print("B. Bandits")
            print("C. Warriors")
            ("\n")
            while True:
                team_choice = input(" ")
                if team_choice != "a" and team_choice != "b" and team_choice != "c":
                    print("Invalid team choice, please choose one of the above options.")
                    continue
                else:
                    break
                        
        
       
            team_selected = None
            for team in balance_teams(players_data, teams_data):
                if team['name'].lower() == teams_data[ord(team_choice.lower()) - ord('a')].lower():
                    team_selected = team
                    break
            
            if team_selected:
                print(f"Team:", team_selected['name'])
                ("\n-----------------------\n")
                players_on_team = len(team['players']['experienced']) + len(team['players']['non_experienced'])
                print("Total players:", team_selected['players_on_team'])
                print("Total experienced:", len(team_selected['players']['experienced']))
                print("Total inexperienced:", len(team_selected['players']['non_experienced']))
                print("Average height:", team_selected['average_height'])
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
    


    
     
     

            

    




