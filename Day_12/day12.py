import random
import os

logo = r"""
   ___                       _____ _                 _                 _.              
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
"""

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
    
def guessing_numbers():
    play = "y"
    while play == "y":
        clear_console()
        print(logo)
        print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
        
        number = random.randint(1, 100)
        
        difficulty = input(r"""Choose a difficulty level. Type "easy" or "hard": """)
        
        if difficulty == "easy":
            attempts_left = 10
        elif difficulty == "hard":
            attempts_left = 5
        
        while attempts_left > 0:
            print(f"You have {attempts_left} attempts remining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high.\nGuess again.")
                attempts_left -= 1
            elif guess < number:
                print("Too low.\nGuess again.")
                attempts_left -= 1
            else: 
                print(f"You got it! The answer was {number}")
                break
                play = input(f"""Wanna play again. Type "y" or "n": """)
        play = input(f"""Wanna play again. Type "y" or "n": """)

################ MAIN ##################
guessing_numbers()
