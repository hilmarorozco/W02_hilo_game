# W02_hilo_game
Class Name: Programming with Classes <br>
Class Code: CSE 210 <br>

# Description
The whole project was written in Python. The game goes like this:
1. At the beginning of the game, you have 300 points.
2. You are given a card number between 1 to 14.
3. You guess if the next card is going to be a higher or lower number than the first card.
4. If you guess correctly, you are given 100 points. However, if you fail to guess, you loose 75 points.
5. The program will ask you if you want to keep playing.
6. The game ends if you do not want to keep playing or if you loose all your points. <br>

# Project Structure
There are four files in the folder: main, director, card, calculate_score. Main imports class Director and starts the game. Class Director is responsible for controlling the sequence of play. Class Card is responsible for generating a random card number for card one and card two. As the game requires it, class Card also gives the number of card two to card one. Class Calculate_score is responsible for keeping track of the player's points, by subtracting and adding according to if the user got it right or wrong. Class Card and class Calculate_score are stand alone classes that are accessed by class Director. <br>

# Required Software
A terminal to be able to play the game. <br>

# Author
Hilmar Orozco <br>
oro18005@byui.edu
