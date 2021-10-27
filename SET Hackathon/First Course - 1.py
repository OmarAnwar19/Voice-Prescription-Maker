from random import randint
game_run = True
game_record = []

def calc_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

def game_over(victor_name):
    print(F"{victor_name} Won!")

while game_run == True:   

    round_counter = 0

    new_round = True

    player = {"name": "", "attack": 13, "heal": 16, "health": 100}
    monster = {"name": "", "attack_min": 10, "attack_max": 20, "health": 100}

    print("---" * 7)
    print("Enter Player Name")
    player["name"] = input()
    print("")

    print("Enter Monster Name")
    monster["name"] = input()
    print("")

    print("Hello, ", player["name"], "!")
    print(player["name"], " Health = ", player["health"])
    print(monster["name"], " Health = ", monster["health"])

    while new_round == True:

        round_counter = round_counter + 1

        player_win = False
        monster_win = False

        print("---" * 7)
        print("Please select action", "\n")
        print("1) Attack")
        print("2) Heal")
        print("3) Exit Game")
        print("4) Show Previous Results")

        action_choice = input()
        print ("")

        if action_choice == "1":

            monster["health"] = monster["health"] - player["attack"]

            if monster["health"] <= 0:
                player_win = True

            else: 

                player["health"] = player["health"] - calc_monster_attack(monster["attack_min"], monster["attack_max"])

                if player["health"] <= 0:
                    monster_win = True

            print(player["name"], " Attacks!")
            print(monster["name"], " Attacks!", "\n")

        elif action_choice == "2":
 
            player["health"] = player["health"] + player["heal"]

            player["health"] = player["health"] - calc_monster_attack(monster["attack_min"], monster["attack_max"])

            if player["health"] <= 0:
                monster_win = True

            print(player["name"] + " Heals")


        elif action_choice == "3":
            game_run = False
            new_round = False

        elif action_choice == "4":
            for i in game_record:
                print(i)
                
            print("")

        else:
            print ("Invalid Input")


        if player_win == False and monster_win == False:
            print(monster["name"], "Health = ", monster["health"], "\n" )

            print(player["name"], "Health = ", player["health"], "\n")

        elif player_win:
            game_over(player["name"])

            round_data = {"winner_name": player["name"], "health": monster["health"], "rounds": round_counter}
            game_record.append(round_data)

            new_round = False

        elif monster_win:
            game_over(monster["name"])

            round_data = {"winner_name": monster["name"], "health": monster["health"], "rounds": round_counter}
            game_record.append(round_data)

            new_round = False
