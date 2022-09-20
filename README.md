## HANGMAN Game

![screenshot](assets/images/readme/responsive.png)

Hangman is an old school favorite, a word game where the goal is simply to find the missing word.You will be presented with a number of blank spaces representing the missing letters you need to find.Use the keyboard to guess a letter. Guessing a new letter each go, if you choose correct, the terminal will tell you and show you where it belongs in the randomly chosen word, if your guess is wrong, then start to draw "hangman" until it is complete.

The actual words are chosen randomly from many words. The game gives number of guess equal to the length of the word. 

## How to play
   1. Please enter valid options like 1,2,3 to play the game
   2. Enter valid name i.e name contains only alphabet and minumum 2 letter
   3. Guess only single alphabet letter and number of guess is eaual to the length of  the actual word
   4. If guessed letter is not found in the actual word then you loose one number of  guess and display the hangman based on the number of life remaining
   5. If guessed letter is already gussed previously then try to guess another letter and you wont loose the number of guess
   6. If guessed letter and actual word are same then you won the game
   7. If number of guess is zeor and guessed letter and actual word are not same then you loose the game    

## Business goals of the website 
This website is developed as part of the third project in diploma in Software Development from The Code Institute and this project mainly focued on the python logic and familier with python language.

A live version of this website will be found here: https://hangman-gameapp.herokuapp.com/


## Table of Contents ##

- [HANGMAN Game](#hangman-game)
- [How to play](#how-to-play)
- [Business goals of the website](#business-goals-of-the-website)
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [Strategy](#strategy)
  - [User Demographic](#user-demographic)
  - [User Stories](#user-stories)
    - [Existing Members](#existing-members)
    - [New Users](#new-users)
  - [User Goals](#user-goals)
  - [Scope](#scope)
  - [Design](#design)
  - [Flowchart](#flowchart)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
------------------------------------------------------------------------------------------------------------

## UX

### Strategy

This Game is ment for:

 - Fun activity 
 - Guess word puzzle
 - Help to improve vocabulary 
 - As the rules are easy, kids can enjoy
 - Any age person can enjoy the game 

What user looking for?
 - Easy to understand the game rules
 - Easy to play using the button and instructions
 - Numbe of guess left and user guessed letters should be visible
 - User shoud know if any thing goes wrong by showing clear message
 - Once the game is over it should show user won or lost
 - Player want to go for next level
 - Player wanr option to enter their name on the score board

Based on all the above requirements, built the game in such a way that 
  - Option Help give the detail instructions which make game easy to play
  - Clear message tells the user what to do next during the game 
  - Guessed word, number of guess left, previously guessed letters visible always to the user 
  - Display the message that player won or loose game
  
### User Demographic

 This application has been designed for users of all ages just for some fun, to test their knowledge and this game help to improve vocabulary

### User Stories

#### Existing Members

 - As a Member: I want to play the game easily
 - As a Member: Need to select mode of game like easy, medium and hard
 - As a Member: I wan to see player won or loose the game
 - As a member: Need to save number of guess took to predict the word

#### New Users

 - As a new User: I want to know how to play the game.
 - As a new User: I want to the look and feel of the game and instructions should be simple.
 - As a new User: I want to see and share the last 10 highest scores using social medias .

### User Goals

 - Easy to use the game by using keyboard with the help of instructions
 - Rules should be clear and concise information to the player 
 - Number of guess left, predicted word and previously gussed letters should be visible to   the player

### Scope

HangMan is a game which guess the letters in the secret word to solve the puzzle aims to familarize with python language and inbuilt libraries.The objective is to build a fun, interactive game for individuals of all ages.

Users may play a fun and exciting game of HungMan against the computer and after each guess, plyaer will clearly know the number guess left to finish the game.

### Design

HangMan project's design has been influenced by the ”Portfolio Project 3 Scope” and "Love sandwitches" - projects.
My design of the project's functionality, coding styles and comments influenced by my previous project "Rock Paper Scisssors".

Main aim is to create a interactive clean and simple interactive terminal where there is a user to get clear info regarding the game in each step.

HangMan is a simple game which has three pages rule.py module exlain how to play the game words.py moduke has list of words and run.py module contain the core functionality of the game. Computer pick the word randomly from words.py and ask the user to guess a letter.Game give three options like play Game, Help and Exit Game. 

### Flowchart
![screenshot](assets/images/readme/flowchart.png)

[Back to top](#hangman-game)

## Features 
![Game](assets/images/readme/fullscreen.png)
HangMan is a single page game that consists of these sections:

 - Landing page with main menu
 - Play Game 
 - Help
 - Exit   
 - Game info contains no of guess left, previously guessed letters and predict word
 - Message

### Existing Features

<details><summary> Landing page </summary>

![Landing page](assets/images/readme/)

 The user is firstly presented with a menu page, showing the options for the game. 
  1 -> Play Game
  2 -> Help
  3 -> Exit Game
</details>
<details><summary>Play Game </summary>

![Play Game](assets/images/readme/)
 When you select option 1 in the main menu, the game will start. First, the user will get a request for a name, which will be added to the Winner's board if they win at the end of the game.
 validate the name based on the below rule
 - Name should contain only alphabets
 - Name should contain atleast 2 letters 

![screenshot](assets/images/readme)

- Current word selected and displayed as "-------".
- Display number of guess left
- Display previously guessed letters  

![screenshot](assets/images/readme)

- For each wrong guess and a part of hangman displayed based on the number of guess left.

![screenshot](assets/images/readme)
![screenshot](assets/images/readme)

- Every correct guess is displayed, add the letter to prevously guessed letters and place the letter in correct position in the current word.

![screenshot](assets/images/readme)

- Once the number of guess become zeor or user predicts the word correctly then the game finished and will display whether they've won or lost, either way the user can see the whole word displayed.

![screenshot](assets/images/readme)
![screenshot](assets/images/readme)


</details>

<details><summary>Help Option </summary>

![Help](assets/images/readme/)

 - After selecting 'Help' from the main menu, it will display the procedure to display the game in detail. 

</details>
<details><summary>Exit Game </summary>

![Exit](assets/images/readme/)

 - If user want to exit the game, he can use this option from the main menu. This will take the user out of the game application and inform the user he left the game app
  
</details>
<details><summary> Game info section </summary>

![Game info section](assets/images/readme/)

 - The game info section is on the first page and it always visible to the user after starting the game.
 - This area contains number of guess left, previously guessed letters and incomplete word 

</details>
<details><summary> Info section </summary>

![Rules](assets/images/readme/)
 
 - This section display the message to the user to proceed the game
 - Game handled all error case like validating the user input for menu selection, input for guess the letter, and input for the name.
 - All the above cases user will get the proper message and action plan
 - In addition to the above validation handled try-- except block as well  
</details>

### Future Features

- To add different mode for the game like easy, medium and hard.
- To add an option for sharing last ten high score on social medias.
- To store player name and their succes based on the number guess they made to predict the word
  
[Back to top](#hangman-game)
