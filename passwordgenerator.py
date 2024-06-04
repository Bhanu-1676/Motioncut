import random
import string

def passwordgenerator(length):
    """Generate a random password of specified length."""
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # Character set: uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices from all_chars
    password += random.choices(characters, k=length - 4)

    # Shuffle the result to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the length of the password: "))
        password = passwordgenerator(length)
        if password:
            print("The Generated password is:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
main()
