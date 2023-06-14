import string
import random

def generate_password(length, complexity, include_special_chars):
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation

    if complexity == 'low':
        password = ''.join(random.choice(characters) for _ in range(length))
    elif complexity == 'medium':
        password = ''.join(random.choice(characters + string.punctuation) for _ in range(length))
    elif complexity == 'high':
        upper = random.choice(string.ascii_uppercase)
        lower = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special = random.choice(string.punctuation) if include_special_chars else ''
        remaining_length = length - 4 if include_special_chars else length - 3
        password = upper + lower + digit + special + ''.join(random.choice(characters) for _ in range(remaining_length))
    else:
        return "Invalid complexity level."

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

# Prompt the user for input
length = int(input("Enter the desired length of the password: "))
complexity = input("Enter the complexity level (low/medium/high): ")
include_special_chars = input("Should special characters be included? (yes/no): ")

# Convert user's input to lowercase for consistency
complexity = complexity.lower()
include_special_chars = include_special_chars.lower()

# Validate complexity level input
if complexity not in ['low', 'medium', 'high']:
    print("Invalid complexity level.")
else:
    # Validate special characters input
    if include_special_chars not in ['yes', 'no']:
        print("Invalid input for special characters.")
    else:
        include_special_chars = include_special_chars == 'yes'
        password = generate_password(length, complexity, include_special_chars)
        print("Generated password:", password)
