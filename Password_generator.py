#RANDOM PASSWORD GENERATOR 
import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return
    
    # Define the character categories
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Ensure the password has at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with a mix of all categories
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Return the password as a string
    return ''.join(password)

# Input: Desired password length from the user
length = int(input("Enter the desired password length (e.g., 8, 12, 16): "))
password = generate_password(length)

# Output: Display the generated password
if password:
    print("Generated Password:", password)
  
