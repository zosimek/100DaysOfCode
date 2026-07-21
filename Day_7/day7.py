import random
import sys



intro_img = """ 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
                   
"""

hangman_0 = r"""
 
 
   
     
    
 
"""

hangman_1 = r"""
 
 
   
     
    
/ 
"""

hangman_2 = r"""
 
 
   
     
    
/ \
"""

hangman_3 = r"""

 |     
 |     
 |     
 |    
/ \
"""

hangman_4 = r"""
 +-----+
 |     
 |     
 |     
 |    
/ \
"""

hangman_5 = r"""
 +-----+
 |     |
 |     
 |     
 |    
/ \
"""

hangman_6 = r"""
 +-----+
 |     |
 |     O
 |     
 |    
/ \
"""

hangman_7 = r"""
 +-----+
 |     |
 |     O
 |     |
 |    
/ \
"""

hangman_8 = r"""
 +-----+
 |     |
 |     O
 |    /|
 |    
/ \
"""

hangman_9 = r"""
 +-----+
 |     |
 |     O
 |    /|\
 |    
/ \
"""

hangman_10 = r"""
 +-----+
 |     |
 |     O
 |    /|\
 |    / 
/ \
"""

hangman_11 = r"""
 +-----+
 |     |
 |     O
 |    /|\
 |    / \
/ \
"""

hangman_states = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6, hangman_7, hangman_8, hangman_9, hangman_10, hangman_11]
lives = 11
miss  = 0

# load the words
with open("500_basic_words.txt", "r", encoding="utf-8") as file:
    words = [line.strip() for line in file if line.strip()]

# choose word
word = random.choice(words)
word_len = len(word)
hidden_word = ["_"] * word_len
hidden_word = list(hidden_word)
letters_tried = []


def round_of_hangman(word, hidden_word, lives, miss, hangman_states):
    print("*************** " + str(lives - miss) + "/" + str(lives) + "LIVES LEFT ***************")
    print(hangman_states[miss])
    
    print("Word to guess: " + " ".join(hidden_word))
    letter = input("Guess a letter: ")
    letters_tried.append(letter)
    
    indexes = [index for index, letters in enumerate(word) if letters == letter]
    if len(indexes) == 0:
        miss += 1
    else:
        for idx in indexes:
            hidden_word[idx] = letter
    print("Word to guess: " + " ".join(hidden_word))
    print("Letters tried: " + ", ".join(letters_tried))
    return hidden_word, lives, miss

### MAIN 
print(intro_img)
while miss != lives and "_" in hidden_word:
    hidden_word, lives, miss = round_of_hangman(word, hidden_word, lives, miss, hangman_states)
    
if miss == lives:
    print("*********************** IT WAS " + word +"! YOU LOSE **********************")
else:
    print("************* CONGRATULATIONS! IT WAS " + word +"! YOU WIN ****************")
sys.exit()
