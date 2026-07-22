######################## IMPORTS ################################
import os

######################## STATICS ################################

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


######################## FUNCTION ###########################

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def bidding_round(continue_bidding = True, bidding_dic = {}):
    while continue_bidding:
        clear_console()
        print(logo)
        print("Welcome to the secret auction program.")
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: PLN "))
        bidding_dic[name] = bid
        answer = input(r"""Are there any other bidders? Type "yes" or "no".""") 
        continue_bidding = False if answer == "no" else True
    return bidding_dic


def find_higher_bidder(bidding_dic):
    winner = max(bidding_dic, key=bidding_dic.get)
    highest_bid = bidding_dic[winner]
    print(f"The winner is {winner} with a bid of {highest_bid} PLN.")
    
########################## MAIN #############################

bidding_dic = bidding_round()
find_higher_bidder(bidding_dic)
              


