
MAX_TRIES = 6
HANGMAN_ASCII_ART = """welcome to the game hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

print(HANGMAN_ASCII_ART, '\n', MAX_TRIES)

tav = input("guess a letter: ")

if len(tav) > 1 and tav.isalpha():
    print("E1")

elif not tav.isalpha() and len(tav) == 1:
    print("E2")

elif len(tav) > 1 and not tav.isalpha():
    print("E3")

else:
    tav = tav.lower()
    print(tav)

WORD = input("enter a word: ")
Length = len(WORD)
new_str = '_ ' * Length
print(new_str)
