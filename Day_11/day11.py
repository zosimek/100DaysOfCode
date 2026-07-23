"""
Blackjack console game without split option.
"""

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


def compensate_aces(points, points_total):
    while points_total > 21 and 11 in points:
        ace_index = points.index(11)
        points[ace_index] = 1
        points_total -= 10

    return points, points_total


def player_hit(deck, player_cards, player_points, player_points_total):
    next_deal = "y"

    while next_deal == "y":
        # Always recalculate from the current cards
        player_points, player_points_total = calculate_points(player_cards)

        # Change aces from 11 to 1 only when necessary
        while player_points_total > 21 and 11 in player_points:
            ace_index = player_points.index(11)
            player_points[ace_index] = 1
            player_points_total -= 10

        print(
            f"Your cards: {player_cards}.\n"
            f"Points: {player_points}\n"
            f"Total points: {player_points_total}"
        )

        if player_points_total >= 21:
            next_deal = "n"
        else:
            next_deal = input(
                'Type "y" to get another card, type "n" to pass: '
            ).lower()

            if next_deal == "y":
                player_cards.append(deal_cards_additional(deck))

    return player_points, player_points_total



def calculate_points(cards):
    points   = []
    
    for card in cards:
        points.append(card_values[card])
    points_total = sum(points)
    
    return points, points_total

#########
def blackjack_game(cards = cards, continue_game = True):
    while continue_game:
        
        print(logo)
        deck = cards 
        
        print("Welcome to Blackjack! Wish you best of luck :-)\n To win collect a total of 21 points or be closer to this number than your oponent.")
        player_cards   = deal_cards_initial(deck)
        computer_cards = deal_cards_initial(deck)
        
        player_points, player_points_total = calculate_points(player_cards)
        computer_points, computer_points_total = calculate_points(computer_cards)
        computer_points, computer_points_total = compensate_aces(computer_points, computer_points_total)
        
        print(f"Computer's first card: {computer_cards[0]}\n Points: {computer_points[0]}\n")
        
        # part when the player can hit (take another card)
        player_points, player_points_total = player_hit(deck, player_cards, player_points, player_points_total)
        
        # computer (dealer) card draw
        while computer_points_total < 17:
            computer_cards.append(deal_cards_additional(deck))
        
            computer_points, computer_points_total = calculate_points(computer_cards)
        
            computer_points, computer_points_total = compensate_aces(
                computer_points,
                computer_points_total
            )
            
        player_diff = abs(21 - player_points_total)
        computer_diff = abs(21 - computer_points_total)
        if (player_points_total <= 21 and player_diff < computer_diff) or (computer_points_total > 21 and player_points_total <= 21):
            print(f"Congtatulations! You win! You had {player_points_total} and computer had {computer_points_total}.\n Computer's cards: {computer_cards}. Computer's points: {computer_points}.")
        elif player_points_total <= 21 and player_diff == computer_diff:
            print(f"Push! You and the computer had the same number of points: {player_points_total}.\n Computer's cards: {computer_cards}. Computer's points: {computer_points}.")
        else:
            print(f"Bad luck mate! You loose! You had {player_points_total} and computer had {computer_points_total}.\n Computer's cards: {computer_cards}. Computer's points: {computer_points}.")

        answer = input(r"""Do you want to play a game of Blackjack again? Type"y" or "n": """) 
        continue_game = False if answer == "n" else True
    
########################## MAIN #############################
blackjack_game(cards = cards, continue_game = True)