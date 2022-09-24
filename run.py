import random
import os
from string import ascii_letters
from termcolor import colored
from words import list_of_words
from hangman import hangman_images
import gspread
from google.oauth2.service_account import Credentials
from help import get_game_help

# Global variable declaration

# For accessing google sheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman-game-score")
scores_sheet = SHEET.worksheet("higher-score")


def display_top_5_score():
    """
    * This function get all datas ie 5 list from the
      score sheet
    * Display name and their scores in proper manner   
    """
    # Get all saved players and their score from the sheet
    total_list_players_from_sheet = scores_sheet.get_all_values()
    # Display players name and their score in table format
    print(colored("\n\n Top five scorers are ...", 'yellow', attrs=['bold']))
    print(colored("________________________________________________________________", 'white', attrs=['bold']))
    print('{:43s} {:20s} '.format(colored("  Name", 'blue', attrs=['bold']), colored("Number of life used", 'blue', attrs=['bold'])))
    print(colored("________________________________________________________________", 'white', attrs=['bold']))
    
    for player in total_list_players_from_sheet:
        print('{:47s} {:20s}  '.format(colored("  "+player[0], 'magenta', attrs=['bold']), colored(player[1], 'magenta', attrs=['bold'])))
    print(colored("________________________________________________________________\n", 'white', attrs=['bold']))
    print(" " * 24 + colored("\n Please enter", 'blue', attrs=['bold']),
          colored("any letter", 'white', attrs=['bold']), 
          colored("or", 'blue', attrs=['bold']), 
          colored(" Enter", 'white', attrs=['bold']),
          colored("to return to main menu...\n", 'blue', attrs=['bold']))
    try:      
        input("\n ")
    except BaseException:
        pass
    main()   


def update_current_score_in_toplist(number_of_life_used, player_name):
    """
    * This function checks current value of number_of_life_used is
      smaller than in top 5 list of score sheet
    * If it smaller then added to sheet at current position
    * If the sheet is empty or contain less than 5 entries then need to
      add the current score to the score sheet 
    """
    # Bydefault the total number of entry in the score sheet is 5
    total_no_of_entry_scoresheet = 5
    # Get all saved players and their score from the sheet
    total_list_players_from_sheet = scores_sheet.get_all_values()
    # Current no of entries in the sheet
    curent_no_of_entry_scoresheet = len(total_list_players_from_sheet)
    index = 0
    
    for index in range(curent_no_of_entry_scoresheet):
        isPresent = False
        # if the current score is less than in the list, then update the current
        # score in the sheet 
        if number_of_life_used <= int(total_list_players_from_sheet[index][1]):
            isPresent = True
            scores_sheet.delete_rows(index+1)
            scores_sheet.insert_row([player_name, number_of_life_used], index+1)
            print(colored(" You score are updated in ", 'green', attrs=['bold']),
                  colored(f"{index+1}", 'white', attrs=['bold']),
                  colored("out of ", 'green', attrs=['bold']),
                  colored("5", 'white', attrs=['bold']))
            break
        else:
            continue
    index += 1
    # if the current no of entries in the sheet is less than 5
    # then append the current score to the sheet 
    if index < total_no_of_entry_scoresheet and isPresent == False:
        scores_sheet.append_row([player_name, number_of_life_used])
        print(colored("You score are updated in ", 'green', attrs=['bold']),
              colored("f{index+1}", 'white', attrs=['bold']),
              colored("out of 5 ", 'green', attrs=['bold']))
    # If the current score is not in top 5 list then show the below message
    elif isPresent == False:
        print(colored("Your score is not in the first five top list.\
                        Please try again,'cyan',attrs=['bold']"))


def clear():
    """
    Clear the screen by using system call based on the os
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_name(name):
    """
    * check name contain any number
    * check name conian atleast 2 characters
    * check name conain any special characters
    * uses difference() method of python to validate
    * returen True : name is valid
              False : name is invalid

    """
    if len(name) < 2 or set(name).difference(ascii_letters):
        return False
    else:
        return True


def draw_hangman(number_of_life):
    """
    * This function return the hunmans based on the
      number of life.
    * Hangmans are already defined in hangman.py  
    """
    return hangman_images[number_of_life]


def run_game():
    """
    * All game's logic functions call from here
    * Get the uer name and validate it
    * if name is valid
        get the orginal word and ask the user to guesss letter
    * validate the guessed letter as per the rules
    * if the guess letter is correct then display the gussed letter
      in the orginal word like _ _ _ X_ _ _
    * if user guess is wrong then start draw hangman
    * display the user gussed letters and reduce the chance count
    * if user guessed all letters correctly then user win
    * if user fails to guess all letter then user lose and display
      the hangman

    """
    # get the player name and validate name againts the rules
    while True:
        #print(colored("\nPlease enter your name\n", 'blue', attrs=['bold']))
        print(colored("-"*80, 'cyan'))
        print(colored("\n Name should contain only letters and should not have any special characters", 'magenta'))
        print(colored(" Example:  Deric \n", 'magenta'))
        print(colored("-"*80, 'cyan'))
        try:
            player_name = input(colored("\n\n Enter your name here:  \n", 'blue', attrs=['bold']))
        except BaseException:
            clear()
            print(colored(
                """ \n\n Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a valid name!""", 'cyan'
            ))
            continue
        if validate_name(player_name):
            break
        else:
            clear()
            print(colored(
                """ \n\n Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a valid name!""", 'cyan'
            ))
    # get randomly actual word from list of words
    actual_word = random.choice(list_of_words)
    print(actual_word)
    # define the number of life and it is equal to the length of the actual word
    number_of_life = len(actual_word)
    # store all the user gussed letters for validating user repeating the same letter
    user_guessed_letters = ""
    # store user guess letter
    user_guess_letter = ""
    # if guess is correct then add the letter to user_guessed_word
    user_guessed_word = ""
    # repeat the user guess until the number of life become 0 
    while (number_of_life >= 0):
        # To display gussed letter in the original word like _ _ X _ _
        # display_guss_letter = ""
        # if user guessed letter present in actual word then add guessed 
        # letter else add "_" to the display word
        display_guss_letter = [letter if letter in user_guessed_letters else "_" for letter in actual_word]
        display_guss_letter = ''.join(display_guss_letter)
        # check the user guessed all letters in the actual word
        if (display_guss_letter == actual_word):
            clear()
            number_of_life_used = len(actual_word) - number_of_life
            print(colored("\n Congratz You Won : You gussed the word",
                  'green', attrs=['bold']), colored(f"{actual_word}", 
                  'white', attrs=['bold']), colored(" using",
                  'green', attrs=['bold']), colored(f"{number_of_life_used}", 
                  'white', attrs=['bold']),
                  colored(" lifes", 'green', attrs=['bold']))
            # add the current score in to the sheet
            update_current_score_in_toplist(number_of_life_used, player_name)
            # Ask user to continue or exit the game
            print(" " * 24 + colored("\n Please enter", 'blue', attrs=['bold']),
                  colored("any letter", 'white', attrs=['bold']), 
                  colored("or", 'blue', attrs=['bold']), 
                  colored(" Enter", 'white', attrs=['bold']),
                  colored("to return to main menu...\n", 'blue', attrs=['bold']))
            try:    
                input("\n ")
            except BaseException:
                pass
            main()

        # Display the number of life left, actual word and all guessed letters
        print("\n\n")
        print(10* " ", colored(50* '#', 'yellow', attrs=['bold']), "\n")
        print(20* " ", colored("Number of life left  :", 'magenta', attrs=['bold']),    colored(f"{number_of_life}", 'white', attrs=['bold']))
        print(20* " ", colored("Gussed letter        :", 'magenta', attrs=['bold']),    colored(f"{user_guessed_letters}", 'white', attrs=['bold']))
        print(20* " ", colored("Actual word          :", 'magenta', attrs=['bold']),    colored(f"{display_guss_letter}", 'white', attrs=['bold']), "\n")
        print(10* " ", colored(50* '#', 'yellow', attrs=['bold']))
        print("\n\n")
        # number of life =0 means user lose the game
        if number_of_life == 0:
            clear()
            print("\n", 6* ' ', colored("Sorry you failed to guess the word:",
                  'red', attrs=['bold']), actual_word)
            print(draw_hangman(number_of_life))
            # Ask user to continue or exit the game
            print(" " * 24 + colored("\n Please enter", 'blue', attrs=['bold']),
                  colored("any letter", 'white', attrs=['bold']), 
                  colored("or", 'blue', attrs=['bold']), 
                  colored(" Enter", 'white', attrs=['bold']),
                  colored("to return to main menu...\n", 'blue', attrs=['bold']))
            try:
                input("\n ")
            except BaseException:
                pass 
            main()
            
        # Ask user to guess the letter
        try:
            user_guess_letter = input(colored("Guess a letter here : \n", 'blue', attrs=['bold']))
        except BaseException:
            clear()
            print(colored("\n Please enter valid character \n", 'red'))
            continue
        # check whether the guess letter is previosly gusses
        if user_guess_letter in user_guessed_letters:
            clear()
            print(colored("\n You already guessed the letter:", 'cyan'),
                  user_guess_letter)
            print(colored("\n Please guess another letter", 'cyan'))
            continue
        # validate the user guessed letter
        if (user_guess_letter in ascii_letters):
            user_guessed_letters += user_guess_letter
        else:
            clear()
            print(colored("\n Please enter valid character \n", 'red'))
            continue

        # user_guess_letter = input("Guess a letter here : ")
        # if guessed letter not present in present in actual word then
        # decrement the number of life and draw hangman
        if user_guess_letter not in actual_word:
            clear()
            print(draw_hangman(number_of_life))
            print(colored(" Oho sorry!!  wrong guess,"
                          "Please try again..", 'red'))
            number_of_life -= 1
        else:
            clear()
            print(20* ' ',
                  colored("\n Your guess is correct !!! letter ", 'green'),
                  user_guess_letter, colored(" found in the word \n", 'green'))
            user_guessed_word += user_guess_letter
    

def main():
    """
     * Game execution start here
     * Display the menu options to the user
     * Get the user choice and execute the suitable function
     * Execute  user input validation
    """
    # Before starting the game clear the screen
    clear()
    while True:
        print("\n\n")
        print(colored("+++++", 'blue'), colored(" Welcome to HangMan Game", 'yellow'), colored("+++++ ", 'blue'))
        print("\n\n")

        print(colored("   1.   Play Game   ", 'magenta', attrs=['bold']))
        print(colored("   2.   Help   ", 'magenta', attrs=['bold']))
        print(colored("   3.   High Scores  ", 'magenta', attrs=['bold']))
        print(colored("   4.   Exit Game  ", 'magenta', attrs=['bold']))

        print("\n\n")
        print(colored("+++++  ++++ +++++ +++++ +++++  +++++ ", 'blue'))
        print("\n\n")
        print(colored(" Please enter valid options like 1, 2, 3 "
                      "and 4 \n", 'cyan'))
        # get user input
        try:
            user_choice = int((input(colored(" Enter your choice here "
                              ": \n", 'blue', attrs=['bold']))))
        except BaseException:
            clear()
            print(colored("\n Invalid input. Please enter valid options"
                  "like 1, 2, 3 and 4", 'red'))
            continue
       
        if user_choice == 1:
            clear()
            print("\n\n")
            print(colored("Your game started .... \n", 'green'))
            # start the game
            run_game()
            break
        elif user_choice == 2:
            clear()
            # Game rules and hints to play
            get_game_help()
            main()
            break
        elif user_choice == 3:
            clear()
            # display top 5 scores from the google sheet
            display_top_5_score()
            break
        elif user_choice == 4:
            clear()
            print(colored("Your leaving the game. See you soon"
                          "...\n", 'white', attrs=['bold']))
            # Exit the game              
            exit()
        else:
            clear()
            print(colored("\n Invalid input. Please enter valid options"
                          "like 1, 2, 3 and 4", 'red'))
            # If user enter option greater than 4 , show the error and 
            # ask to enter again
            continue


main()