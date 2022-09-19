import random
import os
from string import ascii_letters
from words import list_of_words
from hangman import hangman_images
import gspread
from google.oauth2.service_account import Credentials

# Global variable declaration
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman-game-score")
scores = SHEET.worksheet("higher-score")

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
        print("Please enter your name\n")
        print("-"*80)
        print("\nName should contain only letters and should not have any special characters")
        print("Example:  Deric \n")
        print("-"*80)

        player_name = input("\n\nEnter your name here:  ")
        if validate_name(player_name):
            break
        else:
            print(
                """Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a valid name!"""
            )
    # get randomly actual word from list of words
    actual_word = random.choice(list_of_words)
    print(actual_word)
    # define the number of guess and it is equal to the length of the actual word
    number_of_guess = len(actual_word)
    # store all the user gussed letters for validating user repeating the same letter
    user_guessed_letters = ""
    # store user guess letter
    user_guess_letter = ""
    # if guess is correct then add the letter to user_guessed_word
    user_guessed_word=""

    # repeat the user guess until the number of life become 0 
    while (number_of_guess > 0):
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
            print(f"\n Congratz You Won : You gussed the word {actual_word}")
            main()

        # Display the number of guess left and all guessed letters
        print("\n\n")
        print(f"Number of guess left :     {number_of_guess}\n")
        print(f"Gussed letter        :     {user_guessed_letters}")
        print(f"Actual word          :     {display_guss_letter}")
        print("\n\n")
        # Ask user to guess the letter
        user_guess_letter = input("Guess a letter here : ")
        # validate the user guessed letter
        if (user_guess_letter in ascii_letters):
            user_guessed_letters += user_guess_letter
        else:
            print("\nPlease enter valid character \n")
            continue

        # user_guess_letter = input("Guess a letter here : ")
        # if guessed letter not present in present in actual word then
        # decrement the number of guess and draw hangman
        if user_guess_letter not in actual_word:
            number_of_guess -= 1
            print(draw_hangman(number_of_guess))
        else:
            print(f"\n Your guess is correct !!!  {user_guess_letter} found \n")
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
        print("+++++ Welcome to HangMan Game +++++ ")
        print("\n\n")

        print("   1.   Play Game   ")
        print("   2.   Help   ")
        print("   3.   Exit Game  ")

        print("\n\n")
        print("Please enter valid options like 1, 2, 3 \n")
        # get user input 
        user_choice = int(input("Enter your choice here : "))

        if user_choice == 1:
            print("\n\n")
            print("Congratzz!! You started your game \n")
            # start the game
            run_game()
            break
        elif user_choice == 2:
            # Game rules and hints to play
            game_help()
            break
        elif user_choice == 3:
            print("Your leaving the game. See you soon..")
            exit()


main()