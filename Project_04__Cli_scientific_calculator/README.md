# Project 4: Ultimate Scientific CLI Calculator 🧮

## Description
This is the fourth project in my 100 Python Projects journey! It is a fully functional Command Line Interface (CLI) Scientific Calculator. Unlike a standard basic calculator, this application handles dynamic inputs (adding/multiplying infinite numbers at once), performs advanced scientific operations (trigonometry, logarithms, exponents), and features a "bulletproof" error-handling engine that prevents the program from crashing if a user types invalid data.

## What I Learned
This project was a massive step forward in application architecture, learning how to handle dynamic data, and protecting programs from user errors.
* **Error Handling (The Safety Net):** I learned how to use `try` and `except` blocks to catch fatal errors (like a user typing text instead of a number) and handle them gracefully without breaking the loop.
* **The `math` Module:** I learned how to import and utilize Python's built-in mathematical engine to calculate complex formulas like square roots, sines, and logarithms.
* **Dynamic Data Collection:** I transitioned from taking simple `x` and `y` variables to using `for` loops and `lists` to allow the user to input an unlimited amount of numbers for addition and multiplication.
* **The D.R.Y. Principle (Don't Repeat Yourself):** I learned how to build custom helper functions (like my number collector) so I didn't have to write the same block of input code multiple times.
* **Complex Routing:** I successfully managed a large `if/elif/else` control flow to route user choices to the correct mathematical functions.

## Key Terms & Concepts Used

* **`import math`:** A command that loads Python's advanced mathematical library into the script.
* **`try / except`:** A structural block that tells Python to "try" to execute dangerous code, and if a specific error occurs, to execute the "except" block instead of crashing the entire program.
* **`ValueError`:** The specific error Python throws when it expects a number but receives text (e.g., trying to run `float("apple")`).
* **Lists (`[]`):** A data structure used to store multiple items in a single variable. I used `.append()` to dynamically add user inputs to a list.
* **`sum()` & `math.prod()`:** Built-in Python tools to instantly add or multiply every number inside a list.
* **`math.radians()`:** A crucial conversion tool used because Python calculates trigonometry in radians, whereas humans typically input degrees.