

def main():
    """
     * Game execution start here
     * Display the menu options to the user
     * Get the user choice and execute the suitable function
     * Execute  user input validation 
    """
    while True:
        print("+++++ Welcome to HangMan Game +++++ \n")
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
            #Game rules and hints to play 
            game_help()
            break
        elif user_choice == 3:
            print("Your leaving the game. See you soon..")
            exit()






main()