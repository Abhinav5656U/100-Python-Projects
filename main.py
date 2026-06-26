def get_valid_word(prompt_text):
    while True:
        user_word = input(prompt_text).strip()
        if user_word.replace(" ", "").isalpha():
            return user_word
        print("Oops! Please enter a real word (no numbers, spaces, or symbols).")


print("Welcome to the Ultimate Mad Libs Generator!\n")

adjective = get_valid_word("Enter an adjective: ")
noun1 = get_valid_word("Enter a noun: ")
verb = get_valid_word("Enter a past-tense verb: ")
noun2 = get_valid_word("Enter another noun: ")

final_story = f"\nOnce upon a time, a {adjective} {noun1} {verb} straight into a {noun2}!"

print(final_story)
