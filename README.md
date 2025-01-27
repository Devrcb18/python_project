# python_project
This repository contains beginner-level Python projects created by me (Devansh Shukla) ,first year undergrad at IIIT Kalyani aspiring to become an aeronautic and robotics engineer. These projects demonstrate my growing interest in programming, problem-solving, and automation. 
Projects includes:

 # Scissor-Paper-Rock Game ✂️📝🪨
 It is a simple yet beautiful implementation of this old game where user can challenge against computer.
   
   ## Follow the on-screen prompts:
          -Enter your choice:
            -1: Scissors ✂️
            0: Rock 🪨
            1: Paper 📝
          -The game will display your move and the computer's move.
          -The winner is determined based on standard game rules:
          -Scissors beats Paper.
          -Paper beats Rock.
          -Rock beats Scissors.
          -Ties are resolved with retries.
          
   ## Tools used:
        #random(generating number which are linked to rock scissors and paper)
         
        #emoji(studied and implemented using the documentation:https://pypi.org/project/emoji/)

   
 # Guess the Number Game 🎮

 ## Features are--
 
     -Single-Player Turns: Two players can play independently, one after the other.
     -Score Tracking: Saves scores in a file named scorebook.txt.
     -View Scores: Easily review all players' scores.
     -Clear Scores: Reset the score history whenever desired.
     -Friendly User Interface: Easy-to-follow instructions and error handling.

## Follow the on-screen prompts:

      Enter names for Player 1 and Player 2.
      Choose an option from the menu:
      1: Player 1 plays.
      2: Player 2 plays.
      3: View the scorecard.
      4: Clear all previous scores.
      5: Exit the game.
  
 # Peter: A Simple Voice Assistant 🎙️

   ## Features of PETER-
   
         -Voice Commands: Responds to voice commands to perform tasks.
         -Web Browsing:
         -Open Google, Instagram, or YouTube.
         -Search for and play YouTube videos.
         -Open Cricinfo for live scores.
         -Jokes: Tells you a random joke.
         -Time: Provides the current time.
         -Alarm: Set an alarm that plays a selected song.
         -Customizable Responses: Modify the responses and voice rate easily.

      
   ## Liberaries used:
   
      -Datetime
      -Webbrowser
      -Pyttsx3
      -Speech_recognition
      -Os
      -Pyjokes
      -Googlesearch
# Quantum Mechanics: Particle in a 1D Box ⚛️

This project models a quantum particle in a one-dimensional infinite potential well (also known as a "particle in a box"). The program calculates and visualizes:
- The energy levels of the particle based on the principal quantum number (`n`).
- The probability density function of the particle in a specified range within the box.

The results are visualized through two plots:
1. **Energy vs Principal Quantum Number**: Displays the energy levels of the particle.
2. **Probability Density**: Shows the probability density of finding the particle at a specific position.

## Features
- **Energy Calculation**: Computes the energy for a given quantum number `n` using the formula for a particle in a box.
- **Probability Density Plot**: Visualizes the probability density of finding the particle at different positions within the box.
- **User Input**: Allows users to define the length of the box (`l`), the principal quantum number (`n`), and the region of observation (`a` to `b`).

## Prerequisites
To run this project, you need the following:
- Python 3.x
- Required libraries: `numpy`, `matplotlib`, and `scipy`

Install the required libraries using:
```bash
pip install numpy matplotlib scipy
