from os.path import exists


# three global variables
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
HANGMAN_PHOTOS = {0: "x-------x",
                  1: """x-------x
|
|
|
|
|""",
                  2: """x-------x
|       |
|       0
|
|   
|""",
                  3: """x-------x
|       |
|       0
|       |
|
|""",
                  4: """x-------x
|       |
|       0
|      /|\\
|
|""",
                  5: """x-------x
|       |
|       0
|      /|\\
|      /
|""",
                  6: """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}


def print_word(secret_word):
    """
    this function prints the secret word in _
    :param secret_word:
    :return:
    """
    new_str = ""
    for i in range(len(secret_word)):
        if secret_word[i] == ' ':
            new_str += " "
            continue
        elif secret_word[i] == '-':
            new_str += " "
            continue
        new_str += " _ "
    return new_str


def starting_screen():
    """
    this function prints the starting screen of the game
    :return: 
    """
    global MAX_TRIES
    global HANGMAN_ASCII_ART
    print(HANGMAN_ASCII_ART)
    return "you have " + str(MAX_TRIES) + " tries"


def check_valid_input(letter_guessed, old_letter_guessed):
    """
    this function checks if the letter that the player 
    guessed id valid
    :param letter_guessed: 
    :param old_letter_guessed: 
    :return: 
    """
    # check if the input is no more than one char long
    if len(letter_guessed) > 1:
        return False
    
    # check if the input is a letter
    elif not letter_guessed.isalpha():
        return False

    # check if the input is already in the list
    elif letter_guessed in old_letter_guessed or letter_guessed.lower() in old_letter_guessed:
        return False
    else:
        return True


def print_list(letters_list):
    """
    this function sorts the lists by alphabetic order
    and prints is with -> before each letter
    :param letters_list: 
    :return: 
    """
    letters_list.sort()
    print(' -> '.join(letters_list))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    this function checks if the char that the player guessed is valid
    and if it wasn't guessed already
    if it was already guessed the function will print X and a sorted 
    list of the letters that the player guessed
    :param letter_guessed:
    :param old_letters_guessed:
    :return:
    """
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
        # check if a letter from the secret word was guessed if yes,
        # add it into a str
        if secret_word[i] in old_letters_guessed:
            new_str += secret_word[i]
        elif secret_word[i] == " ":
            new_str += " "
        # if there is a char that is not a letter in the word replace it with a space
        elif secret_word[i] == '-' or secret_word[i] == '.' or secret_word[i] == ',':
            new_str += " "
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
    # puts the letters of the secret word that the player guessed
    # inside an str and checks if that str is the secret word
    new_str = show_hidden_word(secret_word, old_letters_guessed)
    if new_str == secret_word:
        return True
    else:
        return False


def print_hangman(num_of_tries):
    """
    this function prints the photos of the hangman
    every times the player guess is wrong
    each time it prints a more advanced photo
    :param num_of_tries:
    :return:
    """
    return HANGMAN_PHOTOS[num_of_tries]


def choose_word(file_path, index):
    """
    this function chooses a word from a text file
    with an index given as an input by the player
    :param file_path:
    :param index:
    :return:
    """
    lst = []
    w = 0
    with open(file_path, "r") as file:
        line_count = 0
        file_object = file.read()
        # if the file is one line long split the word by spaces
        words = file_object.split(' ')

        # if the file is few lines long split the word by each line
        lines = file_object.split('\n')
        for _ in lines:
            line_count += 1

        # if the file is more than one line append from lines to lst
        if line_count > 1:
            for i in range(len(lines)):
                if i in lst:
                    continue
                lst.append(lines[i])

        # if the file is 1 line append from word to lst
        else:
            for j in range(len(words)):
                if j in lst:
                    continue
                lst.append(words[j])
        # if index is bigger than lst length keep appending items
        # from the start of the list to the end of it until the index is the same len as lst
        if index > len(lst):
            while index > len(lst):
                lst.append(lst[w])
                w += 1
        # replace every char that is not alpha in lst with " "
        for j in range(len(lst)):
            if '-' in lst[j] or '.' in lst[j] or ',' in lst[j]:
                lst[j] = lst[j].replace('-', ' ')
    return lst[index-1]


def main():
    """
    this program is the game hangman, the player has 6 tries to
    guess the secret word, the program will return WIN! if the player
    managed to guess the secret word in less than 6 tries, if not the
    program will return LOSE!
    :return: win or lose
    """
    subject = input("enter a subject animal/cars/famous/random: ")
    if subject == 'animal':
        print("copy and enter this file path: "r"C:\Users\User\Documents\\animals.txt")
    elif subject == 'cars':
        print("copy and enter this file path: "r"C:\Users\User\Documents\cars.txt")
    elif subject == 'famous':
        print("copy and enter this file path: "r"C:\Users\User\Documents\famous people.txt")
    else:
        print("copy and enter this file path: "r"C:\Users\User\Documents\destination.txt")
    file = input("enter file path: ")
    while not exists(file):
        print("this is the wrong file path, enter the one you were given")
        file = input("enter file path: ")
    num = input("enter an index: ")

    # 3 variables, first is the word that the player need to guess,
    # second is a list where all the letters that are guessed will be put in
    # and the third is the number of tries that the player have played
    secret_word = choose_word(file, int(num))
    secret_word = secret_word.lower()
    old_letters_guessed = []
    num_of_tries = 0

    # global variables that have been given a value before
    global MAX_TRIES
    global HANGMAN_PHOTOS

    # printing all the relevant stuff (starting screen, the hangman, and the secret word as _)
    print(starting_screen())
    print("the game has began " + HANGMAN_PHOTOS[num_of_tries])
    print("your secret word is: " + print_word(secret_word))
    while num_of_tries < MAX_TRIES:
        tav = input("enter a char: ")

        # make char lowercase
        tav = tav.lower()

        # if char not a valid input
        while not check_valid_input(tav, old_letters_guessed):
            try_update_letter_guessed(tav, old_letters_guessed)
            tav = input("enter a char again: ")

        # if char is valid add to list
        old_letters_guessed.append(tav)

        # print secret word each time
        print(show_hidden_word(secret_word, old_letters_guessed))

        # if the char does not exist in the word
        if tav not in secret_word:
            print(':(')
            num_of_tries += 1
            print(HANGMAN_PHOTOS[num_of_tries])
            continue
        # check if the player guessed the secret word
        if check_win(secret_word, old_letters_guessed):
            print('YOU WIN!')
            break
    if not check_win(secret_word, old_letters_guessed):
        print('YOU LOSE!')
        exit()


if __name__ == "__main__":
    main()
