################## IMPORTS #####################
import os
import random
from art import logo, vs
from game_data import data

################## CONSTANTS #####################

################## FUNCTIONS #####################

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    

def higher_lower_game(a = None):
    print(logo)
    print("Guess who has more followers!")
    loose = False
    score = 0
    data_copy = data
    data_count = len(data_copy)
    ii = 0
    while loose == False:
        if a == None:
            a = data_copy.pop(random.randrange(len(data_copy)))
        b = data_copy.pop(random.randrange(len(data_copy)))
        
        print(f"""Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.""")
        print(f"""Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.""")
        answer = input(f"""Who has more followers? Type "A" or "B": """).lower()
        
        if (a["follower_count"] > b["follower_count"] and answer == "a") or (a["follower_count"] < b["follower_count"] and answer == "a"):
            score += 1
            print(f"""You're right! Current score: {score}.""")
            a = b
        else:
            print(f"""Sorry, that's wrong. Final score: {score}.""")
            break
    
    play = input(f"""Wanna play again. Type "y" or "n": """)
    return play
    
    
    
#################### MAIN ########################

play = "y"
while play == "y":
    play = higher_lower_game()