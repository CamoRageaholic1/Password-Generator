This is a Simple password generator.

Ensure you have the latest version of python installed on your machine.

Run the file by using "python Password_Generator.py"
Answer the prompt
Copy New password

** If this doesnt run on your machine for some reason
you can write click and set the default appliction to the python launcher
This will open up a new terminal running the code. **

## Password_Generator ##
    #import string<br>
    import random
    
    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    while True:
        # Usage
        password_length = int(input("Enter the desired password length: "))
        password = generate_password(password_length)
        print("Generated password:", password)

    # Ask user if they want to generate another password
    repeat = input("Press Enter to generate another password or type 'exit' to quit: ").lower()
    if repeat == 'exit':
        break
        
