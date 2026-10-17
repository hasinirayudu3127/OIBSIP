# task 3
import random
import string


def generate_password(length, character_types):
    characters = ""

    if "uppercase" in character_types:
        characters += string.ascii_uppercase

    if "lowercase" in character_types:
        characters += string.ascii_lowercase

    if "numbers" in character_types:
        characters += string.digits

    if "symbols" in character_types:
        characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8 characters.")
            continue

        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter your choices separated by spaces (example: 1 2 3 4): ").split()

        character_types = []

        if "1" in choices:
            character_types.append("uppercase")

        if "2" in choices:
            character_types.append("lowercase")

        if "3" in choices:
            character_types.append("numbers")

        if "4" in choices:
            character_types.append("symbols")

        if len(character_types) < 2:
            print("Error: Please select at least 2 character types.")
            continue

        password = generate_password(length, character_types)

        print("\n----- Generated Password -----")
        print(password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")