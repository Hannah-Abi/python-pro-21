# Write your solution here
import json
file_name = input("file name: ")
with open(file_name) as hockey_file:
    data = hockey_file.read()
players = json.loads(data)
print(f"read the data of {len(players)} players\n")
print("commands:\n0 quit\n1 search for player\n2 teams\n3 countries\n4 players in team\n5 players from country\n6 most points\n7 most goals")

while True:
    command = int(input("command: "))
    if command == 1:
        player_name = input("name: ")
        for player in players:
            if player_name == player["name"]:
                print()
                print(f"{str(player['name']):20}{str(player['team']):6}{player['goals']} + {player['assists']} =  {player['goals']+ player['assists']}")
                print()
    elif command == 2:
        team_list = []
        for player in players:
            team_list.append(player['team'])
        for team in sorted(list(set(team_list))):
            print(team)
        print()
    elif command == 3:
        country_list = []
        for player in players:
            country_list.append(player['team'])
        for country in sorted(list(set(country_list))):
            print(country)
        print()
    elif command == 4:
        team_name = input("team: ")
        print()
        for player in players:
            if player['team'] == team_name:
                print(f"{str(player['name']):20}{str(player['team']):6}{player['goals']} + {player['assists']} =  {player['goals']+ player['assists']}")
        print()   
    elif command == 0:
        break

if __name__ == "__main__":
    pass