import random



class InvalidMove(Exception):
    def __init__(self, move: str):
        self.move = move
        super().__init__(f'Invalid move: "{move}". It has to be 0, 1, or 2.')
        
        
        
paper_icon = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""


rock_icon = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""


scissors_icon = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""



def print_move(move):
    if move == 0:
        print(paper_icon)
    elif move == 1:
        print(rock_icon)
    elif move == 2:
        print(scissors_icon)
    else:
        raise InvalidMove(move)

def round_score(your_move, computer_move, your_score, computer_score):
    if your_move == computer_move:
        pass
    elif (
        (your_move == 0 and computer_move == 1)
        or (your_move == 1 and computer_move == 2)
        or (your_move == 2 and computer_move == 0)
    ):
        your_score += 1
    else:
        computer_score += 1
    return your_score, computer_score
        
print("Welcome to Paper/Rock/Scirssors game.")
your_score = 0
computer_score = 0

while your_score < 3 and computer_score <3:
    your_move = int(input("What do you choose? Type 0 for Paper, 1 for Rock or 2 for Scissors.\n"))
    computer_move = random.randint(0, 2)
    print_move(your_move)

    print("computer chose:")
    print_move(computer_move)
    your_score, computer_score = round_score(
    your_move,
    computer_move,
    your_score,
    computer_score,
    )
    
    print("ROUND SCORE\n YOU vs COMPUTER: " + str(your_score) + "/" + str(computer_score))

if your_score == 3:
    print("You win!")
else:
    print("Computer win :-(")
    
