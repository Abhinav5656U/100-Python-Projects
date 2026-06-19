# Project 2: Number Guessing Game 🎯

## Description
This is the second project in my 100 Python Projects journey! It is an interactive game where the player defines a maximum range, and the computer randomly selects a secret number within that limit. The player has exactly 10 attempts to guess the number, receiving "Higher" or "Lower" hints along the way.

## What I Learned
This project represented a massive step up in logic. I transitioned from simple, straight-line code to dynamic programs that can make decisions and repeat actions. 
* **Modules:** How to bring in outside code (`random`) to give my program new abilities.
* **Type Conversion:** How to convert text inputs into integers so the computer can perform math and comparisons.
* **Loops:** How to use a `while` loop to keep the game running continuously until a specific condition is met (either winning or running out of tries).
* **Conditional Logic:** How to use `if` and `elif` statements to evaluate the player's guess and provide the correct feedback.
* **D.R.Y. Principle:** "Don't Repeat Yourself." I learned how to structure my code so my counter updates efficiently without having to write the same line of code multiple times.

## Key Terms & Concepts Used

* **`import random`:** This loads Python's built-in random module, allowing us to generate unpredictable numbers.
* **`random.randint(a, b)`:** A specific function from the random module that picks a whole number between point A and point B.
* **`int()`:** A function that takes a string (text) and forces it to become an integer (a whole number). This is vital because `input()` always returns text by default.
* **`while` Loop:** A block of code that will repeat itself over and over as long as a certain condition remains `True` (e.g., `while counter < 10:`).
* **`break`:** A powerful command that instantly "shatters" the loop, stopping it entirely. I used this to end the game the moment the player guesses the correct number.
* **Assignment Operators (`+=`):** A shorthand way to add a value to an existing variable. `counter += 1` is the exact same as writing `counter = counter + 1`.