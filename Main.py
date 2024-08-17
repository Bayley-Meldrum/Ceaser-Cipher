import os

pass
def save_to_file(message, folder, filename):
    while True:
        writechoice = input("Do you want to write your output to a file? (Y/N): ")
        if writechoice.upper() == "Y":
            filepath = os.path.join("Cipher Output", folder)
            if not os.path.exists(filepath):
                os.makedirs(filepath)
            filepath = os.path.join(filepath, filename)
            with open(filepath, "a") as file:  # Use "a" mode for appending instead of "w" mode for writing
                file.write(message + "\n")
                break
        else:
            print("Not writing to file.")
            break

while True:
    # Asks the user if they are encrypting or decrypting text
    choice = input("If you are encrypting text, please enter 'E' or 'encrypt'. If you are decrypting text, please enter 'D' or 'decrypt': ")

    # If statement that checks if users are encrypting or decrypting texts
    if choice.upper() in ["D", "E", "ENCRYPT", "DECRYPT"]:  
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
                        shift = int(input("Please input your shift number (1-25): "))
                        if shift >0:  # Check if the shift number is larger than 0 
                            break
                        else:
                            print("Invalid input. Please enter a number between 1 and 25.")
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                if choice.upper() in ["D", "DECRYPT"]: 
                    # Decrypts the text that the user inputs
                    def decrypt(message, shift):
                        result = ""

                        # Traverse text
                        for char in message:
                            # Skip shifting spaces
                            if char.isspace():
                                result += char
                            # Encrypt uppercase characters
                            elif char.isupper():
                                result += chr((ord(char) - shift - 65) % 26 + 65)
                            # Encrypt lowercase characters
                            elif char.islower():
                                result += chr((ord(char) - shift - 97) % 26 + 97)
                            else: 
                                result += char

                        return result
                    
                    
                    # Outputs the text that the user put in, along with a decrypted version and the shift number
                    print("Input Text:", message)
                    print("Shift Number:", shift)
                    decrypted_text = decrypt(message, shift)
                    print("Output Text:", decrypted_text)
                    save_to_file(decrypted_text, "output", "output.txt")
                    break

                elif choice.upper() in ["E", "ENCRYPT"]:
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
                    save_to_file(encrypted_text, "output", "output.txt")
                    break
            
    # Outputs text that tells the user to restart the program if they spelled 'encrypt' or 'decrypt' wrong
    else:
        print("Invalid choice. Please enter either 'E' or 'D' correctly.")

