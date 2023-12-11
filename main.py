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

"""tav = input("guess a letter: ")

WORD = input("enter a word: ")
Length = len(WORD)
new_str = '_ ' * Length
print(new_str)"""


def check_valid_input(letter_guessed, old_letter_guessed):

    if len(letter_guessed) > 1:
        return False

    elif not letter_guessed.isalpha():
        return False

    elif letter_guessed in old_letter_guessed or letter_guessed.lower() in old_letter_guessed:
        return False
    else:
        return True


def print_list(letters_list):
    letters_list.sort()
    print(' -> '.join(letters_list))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):

    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.sort()
        old_letters_guessed.append(letter_guessed.lower())
        return True

    else:
        print('X')
        print_list(old_letters_guessed)
        return False


def main():
    old_letters = ['b', 'a', 'c']
    letter = input("enter a letter: ")
    print(try_update_letter_guessed(letter, old_letters))
    print('\n', old_letters)


if __name__ == "__main__":
    main()
