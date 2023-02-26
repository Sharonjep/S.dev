import random
import string

def generate_password(length):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
      
      # Shuffle the characters to make the password more random
    mixed_characters = random.sample(characters, len(characters))
      
      # Select a random subset of the shuffled characters to form the password
    password = ''.join(random.choice(mixed_characters) for i in range(length))
      
    return password

password = generate_password(16)
print(password)
