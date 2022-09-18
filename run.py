import random
from string import ascii_letters
from words import list_of_words


def validate_name(name):
    """
    * check name contain any number
    * check name conian atleast 2 characters
    * check name conain any special characters
    * uses difference() method of python to validate
    * returen True : name is valid
              False : name is invalid

    """
    print(ascii_letters)
    print(len(name))
    if len(name) < 2:
        print("correct")
    if len(name) < 2 or set(name).difference(ascii_letters):
        return False
    else:
        return True


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
        print("Name should contain only letters and should not have any special characters")
        print("Example: Deric \n\n")

        player_name = input("Enter your name here:\n")
        if validate_name(player_name):
            print("Name is valid")
            break
        else:
            print(
                """Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a valid name!"""
            )
    # get randomly actual word from list of words
    actual_word = random.choice(list_of_words)

    # define the number of guess and it is equal to the length of the actual word
    number_of_guess = len(actual_word)
    # store all the user gussed letters for validating user repeating the same letter
    user_guessed_letters = ""
    # store user guess letter
    user_guess_letter = ""

    # repeat the user guess until the number of life become 0 
    while (number_of_guess > 0):
        # To display gussed letter in the original word like _ _ X _ _
        display_guss_letter = ""
        # if user guessed letter present in actual word then add guessed 
        # letter else add "_" to the display word
        display_guss_letter = [letter if letter in user_guess_letter else "_" for letter in actual_word]
        print(" ".join(display_guss_letter))

        # Display the number of guess left and all guessed letters
        print(f"Number of guess left : {number_of_guess}\n")
        print(f"Gussed letter: {user_guessed_letters}")
        print("\n\n")
        print(f"Actual word:  {' '.join(display_guss_letter)}")

        # Ask user to guess the letter
        user_guess_letter = input("Guess a letter here : ")
        # validate the user guessed letter
        if (user_guess_letter in ascii_letters):
            user_guessed_letters += user_guess_letter
        else:
            print("Please enter valid character \n")
            user_guess_letter = input("Guess a letter here : ")
        # if guessed letter not present in present in actual word then
        # decrement the number of guess and draw hangman
        if user_guess_letter not in actual_word:
            number_of_guess -= 1
            draw_hangman(number_of_guess)
        else:
            print("Your guess is correct !!!  {user_guess_letter} found ")
        


        
    


def main():
    """
     * Game execution start here
     * Display the menu options to the user
     * Get the user choice and execute the suitable function
     * Execute  user input validation 
    """
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
        user_choice = int(input("Enter your choice here : \n"))

        if user_choice == 1:
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