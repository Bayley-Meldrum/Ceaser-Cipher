from functions import obtain_variables
from functions import decrypt

while True:
    # Asks the user if they are encrypting or decrypting text
    choice = input("If you are encrypting text, please enter 'E'. If you are decrypting text, please enter 'D': ")

    # If statement that checks if users are encrypting or decrypting texts
    if choice.upper() == "D":
        obtain_variables()
        decrypt()
        printing()
        

        

    elif choice.upper() == "E":
        # Input validation loop for text containing only letters and spaces
        while True:
            message = input("Please input your message: ")
            if message.strip() == "":
                print("Invalid input. Please enter a message that is not blank or contains only spaces.")
            else:
                break
        
        # Shift input validation loop
        while True:
            try:
                # Asks the user what shift number they would like to use to decrypt their message and stores it as a variable
                shift = int(input("Please input your shift number: "))
                if shift >0:  # Check if the shift number is larger than 0 
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 25.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

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

        # Outputs the text that the user entered, along with the encrypted version and the shift number
        print("Input Text: " + message)
        print("Shift Number: " + str(shift))
        encrypted_text = encrypt(message, shift)
        print("Output Text: " + encrypted_text)

    # Outputs text that tells the user to restart the program if they spelled 'encrypt' or 'decrypt' wrong
    else:
        print("Invalid choice. Please enter either 'E' or 'D' correctly.")
