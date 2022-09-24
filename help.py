from termcolor import colored


def get_game_help():
    """
    * Define the how to play the game 
    * Explain details of the game like invalid entry, error cases
    """
    print(colored("-" * 120,'blue'))
    print('\n')
    print(colored(" " * 30 + "How to play the GAME", 'yellow'))
    rule_list = (
        '\n1: Please enter valid options like 1,2,3 and 4 to play the game'
        '\n'
        '\n#: If user select option 1 then below are the steps to play the'
        'game'
        '\n'
        '\n2: Enter valid name i.e name contains only alphabet and'
        'minumum 2 letter'
        '\n'
        '\n3: Guess only single alphabet letter and number of life'
        'is equal to the length of the actual word'
        '\n'
        '\n4: If guessed letter is not found in the actual word then you'
        'loose one number of life and display the hangman based on'
        'the number of life remaining'
        '\n'
        '\n5: If guessed letter is already gussed previously then try to'
        'guess another letter and you wont loose the number of life'
        '\n'
        '\n6: If guessed letter and actual word are same then you'
        'won the game'
        '\n'
        '\n7: Check the current number of life used is fit in top five in'
        'the google sheet and then added the player name and number of life'
        'used to the google sheet'
        '\n'
        '\n8: If guessed letter and actual word are same then you'
        'won the game'
        '\n'
        '\n9: If number of life is zero and guessed letter and actual word'
        'are not same then you loose the game'
        '\n'
        '\n#: If user select option 2, it shows the game details'
        '\n'
        '\n#: If user select option 3, it shows the top five list of'
        'players details'
        '\n'
        '\n#: If user select option 4, it exit the game')

    print(colored(rule_list, 'cyan'))

    print("\n\n", colored("-" * 120, 'blue'))
    print('\n')
    input(" " * 24 + colored("\n Please enter", 'blue', attrs=['bold']),
          "any letter", colored("or", 'blue', attrs=['bold']), " Enter",
          colored("to return to main menu...\n", 'blue', attrs=['bold']))