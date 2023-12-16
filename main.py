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
HANGMAN_PHOTOS = {1: "x-------x",
    2: """x-------x
|
|
|
|
|""",
    3: """x-------x
|       |
|       0
|
|   
|""",
    4: """x-------x
|       |
|       0
|       |
|
|""",
    5: """x-------x
|       |
|       0
|      /|\\
|
|""",
    6:"""x-------x
|       |
|       0
|      /|\\
|      /
|""",
    7: """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}
# print(HANGMAN_ASCII_ART, '\n', MAX_TRIES)

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


def show_hidden_word(secret_word, old_letters_guessed):
    """
    this function gets a word(string) and a list and returns
    a new string that is combined from the letters that the
    player guessed and _
    :param secret_word:
    :param old_letters_guessed:
    :return:
    """
    new_str = ""
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            new_str += secret_word[i]
        else:
            new_str += ' _ '
    return new_str


def check_win(secret_word, old_letters_guessed):
    """
    this function gets a word and a list and checks
    if the word exists in the list of letters
    :param secret_word:
    :param old_letters_guessed:
    :return:
    """
    new_str = show_hidden_word(secret_word, old_letters_guessed)
    if new_str == secret_word:
        return True
    else:
        return False


def print_hangman(num_of_tries):
    return HANGMAN_PHOTOS[num_of_tries]


def main():
    """data = ("self", "py", 1.543)
    format_string = "Hello %s %s learner, you have only %.1f units left before you master the course!"
    print(format_string % data)"""
    num = 2
    print(print_hangman(num))


if __name__ == "__main__":
    main()
    
