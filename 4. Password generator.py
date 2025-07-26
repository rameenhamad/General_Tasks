# Generationg recomended password of specified length with different charactors
import random,string

# getting charactors from uppercase,lowercase,special charactors
charac = string.printable

try:
    # Secure user input
    length_password = int(input("Enter desired password length: "))
    
    if length_password <= 0:
        print("Length must be a positive integer.")
    else:
        # Generate password using random.choices to allow repeated characters
        password = ''.join(random.choices(charac, k=length_password))
        # printing password

        print("Generated Password:", password)

except ValueError:
    print("Please enter a valid integer.")