######################## IMPORTS ################################
import random

######################## STATICS ################################

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [
    "ace", "ace", "ace", "ace",
    "king", "king", "king", "king",
    "queen", "queen", "queen", "queen",
    "jack", "jack", "jack", "jack",
    "10", "10", "10", "10",
    "9", "9", "9", "9",
    "8", "8", "8", "8",
    "7", "7", "7", "7",
    "6", "6", "6", "6",
    "5", "5", "5", "5",
    "4", "4", "4", "4",
    "3", "3", "3", "3",
    "2", "2", "2", "2"
]

card_values = {
    "ace"  : 11,
    "king" : 10,
    "queen": 10,
    "jack" : 10,
    "10"   : 10,
    "9"    : 9,
    "8"    : 8,
    "7"    : 7,
    "6"    : 6,
    "5"    : 5,
    "4"    : 4,
    "3"    : 3,
    "2"    : 2,
}

######################## FUNCTION ###########################

def deal_cards_initial(deck):
    chosen_cards = random.sample(deck, 2)
    
    for card in chosen_cards:
        deck.remove(card)
        
    return chosen_cards

def deal_cards_additional(deck):
    chosen_cards = random.sample(deck, 1)
    
    for card in chosen_cards:
        deck.remove(card)
        
    return chosen_cards[0]

def calculate_points(player_cards, computer_cards):
    player_points   = []
    computer_points = []
    
    for card in player_cards:
        player_points.append(card_values[card])

    for card in computer_cards:
        computer_points.append(card_values[card]) 
    
    player_points_total = sum(player_points)
    computer_points_total = sum(computer_points)
    
    return player_points, player_points_total, computer_points, computer_points_total
#########
def blackjack_game(cards = cards, continue_game = True):
    while continue_game:
        
        print(logo)
        
        deck = cards
        next_deal = "y"
        deal_count = 1
        
        print("Welcome to Blackjack! Wish you best of luck :-)\n To win colect a total of 21 points or be closer to this number than your oponent.")
        player_cards   = deal_cards_initial(deck)
        computer_cards = deal_cards_initial(deck)
        player_points, player_points_total, computer_points, computer_points_total = calculate_points(player_cards, computer_cards)
        
        while player_points_total <= 21 and computer_points_total <= 21 and next_deal == "y":
            
            player_points, player_points_total, computer_points, computer_points_total = calculate_points(player_cards, computer_cards)
            
            print(f"Your cards: {player_cards}.\nPoints: {player_points}\nTotal points: {player_points_total}")
            print(f"Computer's first card: {computer_cards[0:deal_count]}\n Points: {computer_points[0:deal_count]}")
            if player_points_total < 21 and computer_points_total < 21:
                next_deal = input(r"""Type "y" to get another card, type "n" to pass: """).lower()
                if next_deal == "y":
                    deal_count += 1
                    player_cards.append(deal_cards_additional(deck))
                    computer_cards.append(deal_cards_additional(deck))

        player_diff = abs(21 - player_points_total)
        computer_diff = abs(21 - computer_points_total)
        if (player_points_total <= 21 and player_diff < computer_diff) or computer_points_total > 21:
            print(f"Congtatulations! You win! You had {player_points_total} and computer had {computer_points_total}")
        elif player_points_total <= 21 and player_diff == computer_diff:
            print(f"Push! You and the computer had the same number of points: {player_points_total}")
        else:
            print(f"Bad luck mate! You loose! You had {player_points_total} and computer had {computer_points_total}")

        answer = input(r"""Do you want to play a game of Blackjack again? Type"y" or "n": """) 
        continue_game = False if answer == "n" else True
    
########################## MAIN #############################
blackjack_game(cards = cards, continue_game = True)