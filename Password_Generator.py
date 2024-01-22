import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    # Example usage
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated password:", password)

    # Ask user if they want to generate another password
    repeat = input("Press Enter to generate another password or type 'exit' to quit: ").lower()
    if repeat == 'exit':
        break