while True:
    message = input("Enter a message: ")
    if message == "":
        print("Error. Please enter a message.")
    else:
        break

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
        elif char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrpyted_message += char

    return decrypted_message


# Outputs the text that the user put in, along with a decrypted version and the secret number
print("Input Text:", message)
print("Shift amount:", shift)
decrypted_message = decrypt(message, shift)
print("Output Text:", decrypted_message)
