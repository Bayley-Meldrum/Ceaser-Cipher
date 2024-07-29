while True:
    #asks the user if they want to use the encrypt or decrypt functions of the program
    choice = input("Would you like to encrypt or decrypt? (E/D): ")
    if choice == ["E", "D"]:
        if choice == "D":
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

            # Decrypts the text that the user inputs
            def decrypt(message, shift):
                result = ""

                # Traverse text
                for char in message:
                    # Skip shifting spaces
                    if char.isspace():
                        result += char
                    # Decrypt uppercase characters
                    elif char.isupper():
                        result += chr((ord(char) - shift - 65) % 26 + 65)
                    # Decrypt lowercase characters
                    elif char.islower():
                        result += chr((ord(char) - shift - 97) % 26 + 97)
                    #skip shifting any other characters
                    else: 
                        result += char

                return result

            # Outputs the text that the user put in, along with a decrypted version and the secret number
            decrypted_text = decrypt(message, shift)
            print("Input Text: " + message)
            print("Secret Number: " + str(shift))
            print("Output Text: " + decrypted_text)

        elif choice == "E":
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
    else:
        print("Invalid input. Please enter E or D.")


