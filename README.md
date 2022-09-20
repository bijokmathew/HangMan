## HANGMAN Game

![screenshot](images/responsive.png)

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
