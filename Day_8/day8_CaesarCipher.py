
######################## STATICS ################################
logo = r"""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

####################### FUNCTIONS ###############################
def alphabet_shift(alphabet, shift_number, direction):
    if direction == 1:
        alphabet_shifted = alphabet[shift_number:] + alphabet[0:shift_number]
    elif direction == 2:
        alphabet_shifted = alphabet[-shift_number:] + alphabet[0:-shift_number:]
    return alphabet_shifted
########################## MAIN #################################
run = True

while run == True:
    result = []
    direction = int(input(r"""Type "1" to encrypt or "2" to decrypt: """))
    if direction not in (1, 2):
        print("Please enter either 1 or 2.")
        continue
    
    if direction == 1:
        message = list(input("Type in message to encrypt: "))
        shift_number = int(input("Type the shift number: "))
        alphabet_shifted = alphabet_shift(alphabet, shift_number, direction)
        
        for character in message:
            if character in alphabet:
                index = alphabet.index(character)
                result.append(alphabet_shifted[index])
            else:
                # Preserve spaces, punctuation, and numbers.
                result.append(character)

        
    elif direction == 2:
        message = input("Type in message to decrypt: ")
        shift_number = int(input("Type the shift number: "))
        alphabet_shifted = alphabet_shift(alphabet, shift_number, direction)
        
        for character in message:
            if character in alphabet:
                index = alphabet.index(character)
                result.append(alphabet_shifted[index])
            else:
                # Preserve spaces, punctuation, and numbers.
                result.append(character)
    print("Result:", "".join(result))
    try_again = input(r"""Tyme "y" if you want to go again. Otherwise type "n".""")
    if try_again == "n":
        run = False


