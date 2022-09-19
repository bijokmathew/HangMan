def get_game_help():
    """
    * Define the how to play the game 
    * Explain details of the game like invalid entry, error cases
    """
    print("^" * 80)
    print('\n')
    print(" " * 30 + "How to play the GAME")
    rule_list = (
        '\n1: Please enter valid options like 1,2,3 to play the game'
        '\n'
        '\n2: Enter valid name i.e name contains only alphabet and'
              'minumum 2 letter'
        '\n'
        '\n3: Guess only single alphabet letter and number of guess'
              'is eaual to the length of the actual word'
        '\n'
        '\n4: If guessed letter is not found in the actual word then you'
             'loose one number of guess and display the hangman based on'
             'the number of life remaining'
        '\n'
        '\n5: If guessed letter is already gussed previously then try to'
             'guess another letter and you wont loose the number of guess'
        '\n'
        '\n6: If guessed letter and actual word are same then you'
             'won the game'
        '\n'
        '\n7: If number of guess is zeor and guessed letter and actual word'
              'are not same then you loose the game')

    print(rule_list)

    print("^" * 80, 'white')
    print('\n')
    input(" " * 24 + "Press Enter to return to the menu \n" + ' ' * 39)