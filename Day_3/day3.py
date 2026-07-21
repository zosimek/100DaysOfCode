import sys


class InvalidDirection(Exception):
    def __init__(self, direction: str):
        self.direction = direction
        super().__init__(f'Invalid direction: "{direction}". It has to be "forward", "back", "left" or "right".')


class InvalidTransportation(Exception):
    def __init__(self, lake_transport: str):
        self.lake_transport = lake_transport
        super().__init__(f'Invalid tipping option: "{lake_transport}". It has to be "wait" or "swim".')
        

class InvalidDoor(Exception):
    def __init__(self, door: str):
        self.door = door
        super().__init__(f'Invalid tipping option: "{door}". It has to be "red", "yellow" or "blue".')
        
        

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your misson is to find the treasure.")
direction = input(r"""You're at a cross road. Where do you want to go?
                  Type "forward", "back", "left" or "right"
                  """)
if direction == "back":
    print("Game over :-( You've abbandoned the mission.")
    sys.exit()
elif direction == "forward":
    print("Game over :-( You fell off a cliff.")
    sys.exit()
elif direction == "right":
    print("Game over :-( You entered the forest and were attacked by a bear... Sorry, my bad it was a man.")
    sys.exit()
elif direction != "left":
    raise InvalidDirection(direction)
    sys.exit()
    
lake_transport = input(r"""You've come to a lake. There is an island in the middle of the lake.
                       Type "wait" to wait for a boat. Type "swim" to swim across.
                       """)
if lake_transport == "swim":
    print("Game over :-( The lake was full of piranhas, and you became their dinner.")
    sys.exit()
elif lake_transport != "wait":
    raise InvalidTransportation(lake_transport)
    sys.exit()
    
door = input(r"""You arrive at the island unharmed. There is a house with 3 doors.
             One red one yellow and one blue. Which colour do you choose?
             """)
if door == "red":
    print("Game over :-( The room was on fire — you die.")
elif door == "yellow":
    print("Game over :-( The room was full of toxic waist — you die of poison.")
elif door == "blue":
    print("You win! You've found the treasure.")
else:
    raise InvalidDoor(door)
