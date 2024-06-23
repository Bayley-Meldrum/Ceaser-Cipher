
message = input("Enter a message: ")
shift = int(input("Enter your secret number: "))

def decrypt(message, shift):
    decrypted_message = ""

    # Traverse text
    for char in message:
        # Skip shifting spaces
        if char.isspace():
            decrypted_message += char
        # Decrypt uppercase characters
        elif char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        else:
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)

    return decrypted_message

# Outputs the text that the user put in, along with a decrypted version and the secret number
print("Input Text:", message)
print("Secret Number:", shift)
decrypted_text = decrypt(message, shift)
print("Output Text:", decrypted_text)
