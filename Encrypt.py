# Input validation loop for text containing only letters and spaces
while True:
    message = input("Please enter your text: ")
    if message.strip() == "":
        print("Invalid input. Please enter some text.")
    else: 
        break

# Number input validation loop
while True:
    try:
        # Asks the user what secret number they would like to use to decrypt their message and stores it as a variable
        shift = int(input("Please input your shift number: "))
        if shift > 0:
            break
        else:
            print("Invalid input. Please enter a number larger than 0.")
    except ValueError:
        print("Invalid input. Please enter a number larger than 0.")
# Encrypts the text that the user inputs
def encrypt(message, shift):
    result = ""

    # Traverse text
    for char in message:
        # Skip shifting spaces
        if char.isspace():
            result += char
        # Encrypt uppercase characters
        elif char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

# Outputs the text that the user entered, along with the encrypted version and the secret number
print("Input Text: " + message)
print("Secret Number: " + str(shift))
encrypted_text = encrypt(message, shift)
print("Output Text: " + encrypted_text)
