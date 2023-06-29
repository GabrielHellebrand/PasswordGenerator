import random
import string
import json

def generate_password(length, uppercase, lowercase, numbers, symbols):
    # Initialize an empty string to store the characters
    characters = ''

    # Check if uppercase letters should be included
    if uppercase:
        characters += string.ascii_uppercase
    else:
        # If not, remove uppercase letters from the characters
        characters -= string.ascii_uppercase
    
    # Check if lowercase letters should be included
    if lowercase:
        characters += string.ascii_lowercase
    else: 
        # If not, remove lowercase letters from the characters
        characters -= string.ascii_lowercase
    
    # Check if numbers should be included
    if numbers:
        characters += string.digits
    else: 
        # If not, remove numbers from the characters
        characters -= string.digits
    
    # Check if symbols should be included
    if symbols:
        characters += string.punctuation
    else:
        # If not, remove symbols from the characters
        characters -= string.punctuation
    
    # Check if no character types are selected
    if len(characters) == 0:
        raise ValueError("At least one character type must be selected.")
    
    # Generate the password by randomly selecting characters from the allowed set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user to enter password criteria
length = int(input("Enter the length of the password: "))
uppercase = input("Include uppercase letters? (True/False): ") == "True"
lowercase = input("Include lowercase letters? (True/False): ") == "True"
numbers = input("Include numbers? (True/False): ") == "True"
symbols = input("Include symbols? (True/False): ") == "True"

# Generate the password based on the provided criteria
password = generate_password(length, uppercase, lowercase, numbers, symbols)
print("Generated Password:", password)

def save_password(password):
   
    # Create a dictionary to store the password
    data = {
        "password": password
    }
    
    # Open the file in write mode and save the password as JSON data
    with open("password.json", "w") as file:
        json.dump(data, file)

# Save the generated password to a file
save_password(password)