import random
import string

print("\n--- 🔐 Strong Password Generator ---")

# 1: Get Valid Length
while True:
    try:
        length = int(input("Enter desired password length (minimum 10): "))
        if length < 10:
            print("Password too short! Must be at least 10 characters for security.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# 2: Get Valid Character Types
while True:
    use_upper = input("Include Uppercase letters? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include Lowercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include Numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include Symbols? (y/n): ").strip().lower() == 'y'

    if not (use_upper or use_lower or use_numbers or use_symbols):
        print("Error: You must select 'y' for at least one character type! Try again.\n")
        continue
    break

# 3: Set up Buckets
guaranteed_chars = []
master_pool = ""

if use_upper:
    guaranteed_chars.append(random.choice(string.ascii_uppercase))
    master_pool += string.ascii_uppercase

if use_lower:
    guaranteed_chars.append(random.choice(string.ascii_lowercase))
    master_pool += string.ascii_lowercase

if use_numbers:
    guaranteed_chars.append(random.choice(string.digits))
    master_pool += string.digits

if use_symbols:
    guaranteed_chars.append(random.choice(string.punctuation))
    master_pool += string.punctuation

# 4: Fill the Rest of the Password
remaining_length = length - len(guaranteed_chars)
password_list = guaranteed_chars.copy()

for i in range(remaining_length):
    password_list.append(random.choice(master_pool))

# Step 5: Shuffle and Output
random.shuffle(password_list)
final_password = "".join(password_list)

print(f"\nYour highly secure password is: {final_password}")