# Project 3: Bulletproof Mad Libs Generator 📝

## Description
This is the third project in my 100 Python Projects journey! It is an interactive Mad Libs game that prompts the user for specific parts of speech and weaves them into a pre-written story. Unlike a basic script, this program features a custom "Input Validator" engine that prevents the user from breaking the game with numbers, symbols, or empty inputs.

## What I Learned
This project was all about data sanitization, string manipulation, and building reusable tools. I transitioned from writing simple, straight-line scripts to creating "bulletproof" applications that can handle unpredictable user behavior.
* **Custom Functions:** How to invent my own commands using `def` to make my code modular and strictly follow the D.R.Y. (Don't Repeat Yourself) principle.
* **Input Validation:** How to use an infinite `while True` loop to trap users until they provide the correct type of data.
* **String Methods:** How to clean, modify, and analyze text behind the scenes using built-in Python tools.
* **Edge Cases:** How to anticipate weird user behavior (like typing multiple words with a space) and write logic to handle it gracefully without breaking the validation rules.

## Key Terms & Concepts Used

* **`def`:** Short for "define." Used to create a custom, reusable function (essentially a mini-program inside the main program).
* **`return`:** A powerful command inside a function that passes safe data back to the main program and instantly breaks whatever loop the function is currently running.
* **`.strip()`:** A string method that automatically deletes accidental, invisible spaces from the very beginning and very end of a user's input.
* **`.isalpha()`:** A string method that evaluates text and returns `True` *only* if every single character is a letter of the alphabet. 
* **`.replace()`:** A method used to swap out specific characters. I used `.replace(" ", "")` to temporarily delete spaces out of multi-word inputs (like turning "hot dog" into "hotdog") so that `.isalpha()` could properly evaluate it.
* **F-Strings:** The formatting tool used to seamlessly inject all of my validated variables directly into the final story block.