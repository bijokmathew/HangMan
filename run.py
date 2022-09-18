from string import ascii_letters


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
    while True:
        print("Please enter your name\n")
        print("Name should contain only letters and should not have any special characters")
        print("Example: Deric \n\n")

        player_name = input("Enter your name here:\n")
        # validate the player name againts the rules
        if validate_name(player_name):
            print("Name is valid")
            break
        else:
            print(
                """Hmmm....this doesn't seem right \U0001F914 """
                """ Please make sure to enter a name!"""
            )



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