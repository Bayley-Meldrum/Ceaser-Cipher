while True:
    message = input("Enter a message: ")
    if all(char.isalpha() for char in message):
        break
    else:
        print("Error. Please enter a valid message that only contains letters.")

while True:
    shift = int(input("Enter your secret number: "))
    if shift >0:
        break
    else:
        print("Error. PLease enter a valid number that is greater than 0.")
#function to decrypt the user's message
def decrypt(message, shift):
    decrypted_message = ""

    # Traverse text
    for char in message:
        #if characters are upper case, decrypt using this line of code
        if char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        # If Character's arent upper case, user this line of code to decrpy the message
        else:
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)

    return decrypted_message


# Outputs the text that the user put in, along with a decrypted version and the secret number
print("Input Text:", message)
print("Secret Number:", shift)
decrypted_text = decrypt(message, shift)
print("Output Text:", decrypted_text)
