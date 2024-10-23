import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    password_characters = ''
    
    if use_uppercase:
        password_characters += string.ascii_uppercase
    if use_lowercase:
        password_characters += string.ascii_lowercase
    if use_digits:
        password_characters += string.digits
    if use_special:
        password_characters += string.punctuation

    if not password_characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(password_characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
