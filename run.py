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


def get_top_5_score():
    """
    Get name and number-of life used of top 5 from the
    hangman-game-score sheet and return the same to
    the caller
    """
    # Get all saved players and their score from the sheet
    total_list_players_from_sheet = scores_sheet.get_all_values()
    print("total_list_players_from_sheet =", total_list_players_from_sheet)
    # return top 5 player list
    return total_list_players_from_sheet[:5]


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
    curent_no_of_entry_scoresheet = len(total_list_players_from_sheet)
    print("curent_no_of_entry_scoresheet = ", curent_no_of_entry_scoresheet)
    print("before  total_list_players_from_sheet == ", total_list_players_from_sheet)
    # skip the first row as it is a titles
    #  total_list_players_from_sheet = total_list_players_from_sheet[1:]
    print("hhh total_list_players_from_sheet == ", total_list_players_from_sheet[1][1])
    index = 0
    
    for index in range(curent_no_of_entry_scoresheet):
        isPresent = False
        print("index",index)
        if number_of_life_used <= int(total_list_players_from_sheet[index][1]):
            isPresent = True
            print(index)
            scores_sheet.delete_row(index+1)
            scores_sheet.insert_row([player_name, number_of_life_used], index+1)
            print(f"You score are updated in {index+1} out of 5 ") 
            break
        else:
            continue
    index += 1
    if index < total_no_of_entry_scoresheet and isPresent == False:
        print("index and total_no_of_entry_scoresheet ", index,  total_no_of_entry_scoresheet)
        scores_sheet.append_row([player_name, number_of_life_used])
        print(f"You score are updated in {index+1} out of 5 ")

    elif isPresent == False:
        print("Your score is not in the first five top list.\
                        Please try again ")

def add_to_score_sheet(name, number_of_life_used):
    #get_given_player_score_from_score_sheet(name)
    update_current_score_in_toplist(number_of_life_used, name)


def clear():
    """
    Clear the screen by using system call
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


def draw_hangman(number_of_guess):
    return hangman_images[number_of_guess]


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
        print("\nPlease enter your name\n")
        print("-"*80)
        print("\n Name should contain only letters and should not have any special characters")
        print(" Example:  Deric \n")
        print("-"*80)

        player_name = input("\n\nEnter your name here:  \n")
        if validate_name(player_name):
            break
        else:
            clear()
            print(
                """ \n\n Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a valid name!"""
            )
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
    user_guessed_word=""
    # this variable used to check whtether screen to clear or not
    is_error = False
    # repeat the user guess until the number of life become 0 
    while (number_of_life >= 0):
        # In case of error no need to clear the screen
        if not is_error:
            clear()
        is_error = False
        # To display gussed letter in the original word like _ _ X _ _
        # display_guss_letter = ""
        # if user guessed letter present in actual word then add guessed 
        # letter else add "_" to the display word
        display_guss_letter = [letter if letter in user_guessed_letters else "_" for letter in actual_word]
        display_guss_letter = ''.join(display_guss_letter)
        print(display_guss_letter)
        print(actual_word)
        # check the user guessed all letters in the actual word
        if (display_guss_letter == actual_word):
            number_of_life_used = len(actual_word) - number_of_life
            add_to_score_sheet(player_name,number_of_life_used)
            print(f"\n Congratz You Won : You gussed the word {actual_word} using {number_of_life_used} lifes")
            # Add player name and score to score sheet   
            input("\n Please eneter any letter or 'Enter' to return to main menu...\n")
            main()

        # Display the number of life left, actual word and all guessed letters
        print("\n\n")
        print(10* " ", 50* '#',"\n")
        print(20* " ", f"Number of life left :     {number_of_life}", 20* " ")
        print(20* " ", f"Gussed letter        :     {user_guessed_letters}", 20* " ")
        print(20* " ", f"Actual word          :     {display_guss_letter}", 20* " ","\n")
        print(10* " ", 50* '#', 10*" ")
        print("\n\n")
        # number of life =0 means user lose the game
        if number_of_life == 0:
            print("\n", 6* ' ', f"Sorry you failed to guess the word: {actual_word} ")
            print(draw_hangman(number_of_life))
            input("\n Please eneter any letter or 'Enter' to return to main menu...\n")
            main()
            
        # Ask user to guess the letter
        user_guess_letter = input("Guess a letter here : \n")
        # check whether the guess letter is previosly gusses
        if user_guess_letter in user_guessed_letters:
            print(f"\nYou already guessed the letter: {user_guess_letter}")
            print("Please guess another letter")
            is_error = True
            continue
        # validate the user guessed letter
        if (user_guess_letter in ascii_letters):
            user_guessed_letters += user_guess_letter
        else:
            print("\nPlease enter valid character \n")
            is_error = True
            continue

        # user_guess_letter = input("Guess a letter here : ")
        # if guessed letter not present in present in actual word then
        # decrement the number of life and draw hangman
        if user_guess_letter not in actual_word:
            number_of_life -= 1
            is_error = True
        else:
            print(20* ' ', f"\n Your guess is correct !!!  {user_guess_letter} found \n")
            user_guessed_word += user_guess_letter
            is_error = True
    

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
        print("+++++ Welcome to HangMan Game +++++ ")
        print("\n\n")

        print("   1.   Play Game   ")
        print("   2.   Help   ")
        print("   3.   High Scores  ")
        print("   4.   Exit Game  ")

        print("\n\n")
        print("+++++  ++++ +++++ +++++ +++++  +++++ ")
        print("\n\n")
        print(" Please enter valid options like 1, 2, 3 and 4 \n")
        # get user input 
        user_choice = (input(" Enter your choice here : \n"))
        # validate the user choice and it should contain only number
        if not user_choice.isdecimal():
            clear()
            print("\n Invalid input. Please enter valid options like 1, 2, 3 and 4")
            continue
        else:
            try:
                user_choice = int(user_choice)
            except ValueError():
                clear()
                print("\n Invalid input. Please enter valid options like 1, 2, 3 and 4")
                continue
        if user_choice == 1:
            print("\n\n")
            print("Your game started .... \n")
            # start the game
            run_game()
            break
        elif user_choice == 2:
            # Game rules and hints to play
            get_game_help()
            break
        elif user_choice == 3:
            # display top 5 scores from the google sheet
            get_top_5_score()
            break
        elif user_choice == 4:
            clear()
            print("Your leaving the game. See you soon..")
            exit()
        else:
            clear()
            print("\n Invalid input. Please enter valid options like 1, 2, 3 and 4")
            continue


main()