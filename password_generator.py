import random
import string
# Password Generator in Python
print("Welcome to the Python Password Generator")

try:
    length = int(input("Enter the length of password you want: "))

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    print(f"\n✅ Your Generated Password is:\n{password}")

except ValueError:
    print("Please enter a valid number for length.")
