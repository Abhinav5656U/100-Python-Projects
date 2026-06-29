# Project 5: Strong Password Generator 🔐

## Description
The fifth project in my 100 Python Projects journey! This is a Command Line Interface (CLI) application that generates highly secure, randomized passwords. It forces a minimum length of 10 characters for security and allows the user to customize exactly which character types (Uppercase, Lowercase, Numbers, Symbols) they want to include. 

Crucially, this program doesn't just pull random characters from a giant pool—it uses a "guaranteed bucket" logic system to ensure that at least one of every selected character type is strictly included in the final password before shuffling them together.

## What I Learned
This project was an incredible exercise in data manipulation, list handling, and advanced logic flow.
* **The "Guaranteed Inclusion" Logic:** I learned how to solve the problem of accidental exclusion by building a system that first picks one required character from each selected category, and then fills the rest of the password from a master pool.
* **Inline Boolean Evaluation:** I learned a clever shortcut to turn a user's text input directly into a `True` or `False` variable in a single line (e.g., `input() == 'y'`).
* **The `string` Module:** I utilized Python's built-in string constants (`string.ascii_uppercase`, `string.digits`, etc.) to generate character pools dynamically instead of hardcoding the alphabet or symbols.
* **Advanced List Manipulation:** I learned how to use `.copy()` to safely duplicate lists, and `random.shuffle()` to randomize the order of items within a list to ensure my guaranteed characters weren't always stuck at the beginning of the password.
* **String Assembling:** I learned how to use the `"".join()` method to seamlessly convert a list of individual characters back into a single, clean string.

## Key Terms & Concepts Used

* **`import string`:** Brings in Python's pre-built constants for letters, numbers, and punctuation.
* **Boolean (`True`/`False`):** Data types used to track which character categories the user explicitly enabled.
* **`random.shuffle()`:** A method from the random module that reorganizes the items inside a list into a random order.
* **`.copy()`:** A list method used to create a completely independent clone of an existing list, preventing accidental overwrites.
* **`"".join(list)`:** A powerful string method that takes an iterable (like a list) and glues all of its elements together into one string. The `""` specifies that no spaces or separators should be placed between the characters.